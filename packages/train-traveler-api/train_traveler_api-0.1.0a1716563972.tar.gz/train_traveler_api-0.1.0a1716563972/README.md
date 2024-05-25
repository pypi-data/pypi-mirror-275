# Train Traveler

> **Warning**
> 
> **Train Traveler is currently under construction and is in alpha stage. Use at your own risk. Features and functionality may change.**


**Train Traveler** is a versatile tool for accessing SNCF train information. It provides both a Python module offering a framework to access the SNCF API and an interactive command-line interface (CLI) to retrieve upcoming trains for a specified departure and destination, as well as the last journey of the day.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [As a Python Module](#as-a-python-module)
  - [As a Command-Line Tool](#as-a-command-line-tool)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- **SNCF API Access Framework**: Easily interact with the SNCF API to retrieve train information.
- **Interactive Command-Line Interface**: Quickly get upcoming trains and the last journey of the day via CLI.
- **Custom Searches**: Specify departure and arrival stations to get precise information.
- **Journey History**: Check the last journeys of the day.

## Installation

1. Clone the GitHub repository:

    ```bash
    git clone https://github.com/Matthyeux/train-traveler-api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd train-traveler-api
    ```

## Usage

### As a Python Module

You can use **Train Traveler** as a Python module to interact with the SNCF API in your own scripts.

```python
from sncf.connections.connection_manager import ApiConnectionManager

from sncf.repositories.journey_repository import ApiJourneyRepository 
from sncf.repositories.stop_area_repository import ApiStopAreaRepository
from sncf.repositories.disruption_repository import ApiDisruptionRepository

from sncf.services.journey_service import JourneyService


# Initialize the client with your API key
# url = https://api.sncf.com/v1
# api_key = your api key
# region = sncf
connection = ApiConnectionManager(url, api_key, region)

# Initiatlize journey_service
journey_service = JourneyService(
    stop_area_repository=ApiStopAreaRepository(connection),
    journey_repository=ApiJourneyRepository(connection),
    disruption_repository=ApiDisruptionRepository(connection)
)

departure = Area('stop_area:SNCF:87391003', 'Paris - Montparnasse - Hall 1 & 2 (Paris)', 'Paris - Montparnasse - Hall 1 & 2', {'lon': '2.320514', 'lat': '48.841172'})

destination = Area('stop_area:SNCF:87581009', 'Bordeaux Saint-Jean (Bordeaux)', 'Bordeaux Saint-Jean', {'lon': '-0.556697', 'lat': '44.825873'})

# Get the next trains
# Count is the number of journeys to retrieve
next_trains = journey_service.get_direct_journeys(departure, destination, count=2)

# Get the last train of the day
last_train = journey_service.get_last_direct_journeys(departure, destination)
```

### As a Command-Line Tool

Train Traveler includes a CLI for quick and interactive use.

```bash

# Get the next trains
train-traveler journey --from Paris --to Bordeaux --max-journeys 2

# Get the last train of the day
train-traveler journey --from Paris --to Bordeaux --last-journey
```

## Configuration

To use the SNCF API, you need to obtain an API key from the [SNCF Developer Portal](https://numerique.sncf.com/startup/api/token-developpeur/).


Set your API key by defining the `url`, `region` and `api_key`, in config/auth.yml or by setting:

```bash
export SNCF_API_URL='https://api.sncf.com/v1'
export SNCF_API_REGION='sncf'
export SNCF_API_KEY='your_api_key'
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss the changes you want to make.

    Fork the project
    Create your feature branch (git checkout -b feature/AmazingFeature)
    Commit your changes (git commit -m 'Add some AmazingFeature')
    Push to the branch (git push origin feature/AmazingFeature)
    Open a Pull Request

## License

Distributed under the MIT License. See LICENSE for more information.