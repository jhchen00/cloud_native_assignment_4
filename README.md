# cloud_native_assignment_4

## Quick Start
1. Run the commmand to build a Docker image
```shell
docker build -t simple_calculator .
```

2. Run the command to run the image
```shell
docker run -p 3000:3000 simple_calculator
```

3. Go to the URL using your browser
```shell
http://localhost:3000
```