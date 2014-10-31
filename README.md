**HERE BE DRAGONS**

# twarm
A distributed Docker-powered Python testing framework

## How to use it?
1. Build the Docker container from the image `cd RUNNER` and `docker build .`
2. Run the very hacky Python script, passing a directory and the Docker URL 
`python twarm.py DIR URL`

## Issues
SO MANY ISSUES!

### Specifically...
1. It does not aggregate results. It will dump the results into `DIR/output` 
for each file.
2. If a test goes on till the end of time then it too will go on till the end
of time - no one is left behind.
3. The code is horrible.
