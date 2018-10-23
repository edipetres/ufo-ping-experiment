# Ping times

## Hypothesis

The three servers have vastly different ping times. Likely these servers are located at different proximities from the machine they are contacted from.

## Experiment

I have set up a small experiment to execute an average measurement of the pingtime of these three servers. Run it from terminal: `python ping-experiment.py`. It takes the hostname of each server, runs the `ping` program pinging the servers 5 times. The result is collected and printed out when the program finishes.

## Evaluation

Running the program from Lyngby, Copenhagen, DK prints the following results

```sh
Average round-trip for 5 pings
46.101.253.149: 18.179 ms
128.199.144.199: 239.752 ms
167.99.51.33: 89.374 ms
```

Running the program from a server in Frankfurt

```sh
Average round-trip for 5 pings
46.101.253.149: 1.648 ms
128.199.144.199: 168.690 ms
167.99.51.33: 82.204 ms
```

These results indicate that on average the pingtime does differ for the servers. If run miltiple times, it produces pingtime differences similar in proportion.

When coonducting the expreiment from Frankfurt, the pingtime for server `46.101.253.149` is reduced to only `1.648 ms`. This suggests that host to be a closer proximity to Frankfurt.

We can interpret these numbers to conclude these servers respond from different places due to the constant difference in the time it takes for a round-trip to contact them.

## Discussion

The program we ran for the experiment only shows the average pingtime. It could be of interest to take into consideration the min/max pingtimes as well as the standard deviation. These together would give a better picture of the servers proximity to contacting computer. However, the average time also has a high significance.

These results could be influenced by the network environment of the host computer.