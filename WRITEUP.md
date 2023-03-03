# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

I choose app service over VM for this project because of the following factors

1. VM requires self-management to set up security setup such as firewall and setup of web server etc
2. Deeper Knowledge require to understand servers and OS if we choose VM.
3. We do not need more control over server for this project so, I choose app service.
4. The purpose of this project to host it on azure, so we do not need full-fledged server.
5. We only need limited compute power for this project, so we can choose from A series or DV2 series, but if we choose VM  there are many more such as B, F, E and G series which is not required for this project.
6. Integrated load balancer is available in Azure App Service which can easily increase instances. VM required separate load balancer.
7. Even though the cost of app service is more than VM but there is a free tier plan available for our project so, I choose that plan.
8. App service is not more safe and continues charge but ,we only need to deploy it using udacity account so, it is automatically deleted after completed out work.
9. To handle VM a dedicated team required so app service is best for small scale projects.
10. With VMs, one can also say  “With extra power, comes extra responsibilities”


*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

It boils down to the organization's present capabilities and the project's requirements. At the end of the day, the most important thing is to properly support the company and users.

*URL
https://cmsproject7007.azurewebsites.net/login