# erddaplogs

Try it out on Binder [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/callumrollo/erddaplogs/HEAD?labpath=weblogs-parse-demo.ipynb)

Quick utilities for parsing nginx and apache logs.

This script takes apache and/or nginx logs as input. It is made to analyse visitors to an ERDDAP server, but should work on any web traffic.

The jupyter notebook performs the following steps:

1. Read in apache and nginx logs, combine them into one consistent dataframe
2. Find the ips that made the greatest number of requests. Get their info from ip-api.com
3. Remove suspected spam/bot requests
4. Perform basic anaylysis to graph number of requests and users over time, most popular datasets/datatypes and geographic distribution of users

A blog post explaining this notebook in more detail can be found at [https://callumrollo.com/weblogparse.html](https://callumrollo.com/weblogparse.html)

### A note on example data

If you don't have your own ERDDAP logs to hand, you can use the example data in `example_data/nginx_example_logs`. This is anonymmised data from a production ERDDAPP server [erddap.observations.voiceoftheocean.org](https://erddap.observations.voiceoftheocean.org/erddap). The ip addresses have been randommly generated, as have the user agents. All subscription emails have been replaced with fake@example.com


### License

This project is licensed under MIT.
