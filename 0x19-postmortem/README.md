# Postmortem - Solitaro Server Timing Out

### Issue Summary:

On *14th August, 2023* at exactly *2100 Hrs* in the *UTC* timezone. Our web application experienced an outage that lasted for approximately 50 minutes. The outage resulted in our users not being able to access the site and it affected **40%** of our users.

### Timeline:

[2100]: The issue was first detected when monitoring alerts indicated a significant increase in server response times.

[2105]: Support team observed multiple emails coming from the user complaining of the server taking forever to load the returnig an internal server error.

[2110]: Investigations began by analyzing our servers to see the load on the servers.

[2115]: Assumptions were made that the issue may be related to our servers not being able to handle the load.

[2125]: The incident was escalated to the operations tema for further analysis.

[2140]: Engineers discovered that all the users requests for the site were being forwarded to web-01 instead of balancing them between the two servers.

[2150]: After identifying the root cause, engineers fixed the algorithm to ensure balancing of requests and the service was restarted.


### Root Cause and Resolution

The root cause of the issue was traced back to the algorithm for handling the requests had not been set up correctly. This led to all user requests being handled by one server therefore overloading it with user requests.

To resolve the issue the following steps were taken:

- Haproxy config file  was set up correctly to ensure it was using the correct load balancing algorithm.
- The SRE team wrote an automation script that should configure the load balancer and server properly any time a new server needs to be added.


### Corrective and Preventative Measures:

To prevent similar occurences in the future, the following measures will be implemented:

1. Enforce stricter script review processes to catch and prevent hidden features or unintended behavior.
2. Implement proper automation scripts for every repetitive task.
3. Enhance monitoring and alerting systems to quickly identify unusual patterns or perfomance degradation.

### Conclusion:

The "Server Time Out" incident was a result of improper load balancing technique that momentarily brought downtime to our Solitaro social media app. While it showcased our application's flexibility, it also highlighted the importance of rigorous script reviews and testing. We are committed to continuously improving our development practices and ensuring that unexpected surprises are curbed early rather than impacting our user experience.
