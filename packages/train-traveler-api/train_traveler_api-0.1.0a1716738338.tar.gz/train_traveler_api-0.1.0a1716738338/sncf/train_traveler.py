import os

def main():
    import sys
    
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    import yaml
    import argparse

    def get_auth_info(config_file):
        url = os.getenv('SNCF_API_URL')
        region = os.getenv('SNCF_API_REGION')
        api_key = os.getenv('SNCF_API_KEY')

        if url and api_key and region:
            return url, region, api_key

        if os.path.exists(config_file):
            with open(config_file, "r") as f:
                config = yaml.safe_load(f)

                url = config["connection"]["url"]
                region = config["connection"]["region"]
                api_key = config["connection"]["api_key"]
            return url, region, api_key
        raise RuntimeError("Auth configuration not found. Please set the SNCF_API_URL, SNCF_API_ENV and SNCF_API_KEY environment variable or provide a config/auth.yml file.")
    
    from datetime import timedelta

    from sncf.connections.connection_manager import ApiConnectionManager
    from sncf.repositories.repository_manager import ApiRepository
    from sncf.repositories.place_repository import ApiPlaceRepository
    from sncf.repositories.stop_area_repository import ApiStopAreaRepository
    from sncf.repositories.journey_repository import ApiJourneyRepository
    from sncf.repositories.disruption_repository import ApiDisruptionRepository
    from sncf.repositories.link_repository import ApiLinkRepository

    from sncf.entities.place_entity import PlaceAreaEntity
    from sncf.entities.stop_entity import StopEntity

    from sncf.models.journey_model import Journey

    from sncf.services.journey_service import JourneyService
    from sncf.services.area_service import AreaService

    def format_timedelta(delta: timedelta):
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        if delta.days > 0:
            return f"{delta.days} days"
        elif hours > 0:
            if minutes > 0:
                return f"{hours} hours, {minutes} minutes"
            else:
                return f"{hours} hours"
        else:
            return f"{minutes} minutes"


    def display_place_area_info(place_area: PlaceAreaEntity):
        print("-----------------------------")
        print("Place {place_name} - {place_id}".format(place_name=place_area.name, place_id=place_area.id))
        print("-----------------------------")
        print("Area id: {}".format(place_area.stop_area.id))
        print("Area name: {}".format(place_area.stop_area.name))
        print("Area label: {}".format(place_area.stop_area.label))
        print("Area coord: {}, {}".format(place_area.stop_area.coord["lon"], place_area.stop_area.coord["lat"]))


    def display_journey_info(start: StopEntity, end: StopEntity, journeys: list[Journey]):
        print("-----------------------------")
        print("Next journeys from '{}' to '{}'".format(start.label, end.label))
        print("-----------------------------")
        for journey in journeys:
            print("-----------------------------")
            print("Departure: {}".format(journey.journey.departure_date_time))
            print("Arrival: {}".format(journey.journey.arrival_date_time))
            if journey.journey.status != "":
                print("Status: {}".format(journey.journey.status))
            print("-----------------------------")

            for section in journey.journey.sections:
                print("-- ")
                print("-- Line: {}".format(section.informations.label))
                print("-- n°{}".format(section.informations.trip_short_name))
                print("-- Departure: {}".format(section.departure_date_time))
                print("-- Arrival: {}".format(section.arrival_date_time))
                print("-- Direction: {}".format(section.informations.direction))
                print("-- Type: {}".format(section.informations.physical_mode))
                print("--")
            print("-----------------------------")
            for disruption in journey.disruptions:
                local_message = None
                if disruption.severity_effect == "SIGNIFICANT_DELAYS":
                    for impacted_objects in disruption.impacted_objects:
                        for impacted_stop in impacted_objects.impacted_stops:
                            if impacted_stop.stop_point.name == start.name:
                                delay = format_timedelta(impacted_stop.ammended_departure_time - impacted_stop.base_departure_time)
                                local_message = "{} delay".format(delay)
                elif disruption.severity_effect == "REDUCED_SERVICE":
                    local_message = ""
                    for impacted_objects in disruption.impacted_objects:
                        for impacted_stop in impacted_objects.impacted_stops:
                            if (impacted_stop.arrival_status or impacted_stop.departure_status) == "deleted":
                                local_message += "{}, ".format(impacted_stop.stop_point.label)
                    local_message += "stops are deleted"
                elif disruption.severity_effect == "NO_SERVICE":
                    local_message = "Deleted"
                elif disruption.severity_effect == "MODIFIED_SERVICE":
                    pass
                elif disruption.severity_effect == "ADDITIONAL_SERVICE":
                    local_message = "Added"
                else:
                    print("-- Disruption: {}".format(disruption.severity_effect))

                if local_message:
                    print("-- Message: {}".format(local_message))                
                for message in disruption.messages:
                    print("-- Cause: {}".format(message))



    def journey_help():
        print("Usage of the 'journey' command:")
        print("    sncf-api.py journey --from <start> --to <end> --max-journeys <max>")
        print("Description:")
        print("    This command performs journey operations.")
        print("Options:")
        print("    --from <start>: Starting point of the journey (required)")
        print("    --to <end>: Ending point of the journey (required)")
        print("    --max-journeys <max>: Maximum number of journeys to perform (default: 1)")


    def journey_command(args):
        url, region, api_key = get_auth_info(os.path.join(SCRIPT_DIR, "..", "config", "auth.yml"))
        connection = ApiConnectionManager(url, api_key, region)
        place_repository = ApiPlaceRepository(connection=connection)
        stop_area_repository = ApiStopAreaRepository(connection=connection)
        journey_repository = ApiJourneyRepository(connection=connection)
        disruption_repository = ApiDisruptionRepository(connection=connection)

        area_service = AreaService()
        journeyService = JourneyService(stop_area_repository, journey_repository, disruption_repository)

        start_places_areas = place_repository.find_areas_from_places(args.start)
        end_places_areas = place_repository.find_areas_from_places(args.end)

        for start_area in start_places_areas:
            for end_area in end_places_areas:
                
                if args.last_journey:
                    next_journey = journeyService.get_last_direct_journey(
                        area_service.create_area(start_area.stop_area),
                        area_service.create_area(end_area.stop_area)
                    )
                else:
                    next_journey = journeyService.get_direct_journeys(
                        area_service.create_area(start_area.stop_area),
                        area_service.create_area(end_area.stop_area),
                        count=args.max_journeys
                    )

                if len(next_journey.journeys) > 0:
                    display_place_area_info(start_area)
                    display_place_area_info(end_area)
                    display_journey_info(next_journey.start, next_journey.end, next_journey.journeys)


    parser = argparse.ArgumentParser(description="Command-line interface for sncf-api")
    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

    # Sub-command: journey
    journey_parser = subparsers.add_parser("journey", help="Perform journey operations")
    journey_parser.add_argument("--from", dest="start", required=True, help="Starting point of the journey")
    journey_parser.add_argument("--to", dest="end", required=True, help="Ending point of the journey")
    journey_parser.add_argument("--max-journeys", type=int, default=1, help="Maximum number of journeys")
    journey_parser.add_argument("--last-journey", action="store_true", help="Flag to indicate only the last journey")


    args = parser.parse_args()
    
    if args.command == "journey":
        journey_command(args)
    else:
        journey_help()

if __name__ == "__main__":
    main()


