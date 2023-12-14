# Deployment Resource Analysis: VM vs App Service

For deploying the CMS app, I considered both a Virtual Machine (VM) and an Azure App Service. I focused on four key aspects: costs, scalability, availability, and workflow.

## Costs

- **VM:** Generally offers a lower cost for long-term use, especially with optimizations. However, requires manual setup and maintenance.
- **App Service:** Typically has a higher cost but includes many built-in features, reducing overhead and maintenance costs.

## Scalability

- **VM:** Provides flexible scalability but requires manual scaling and maintenance.
- **App Service:** Automatically scales based on demand, offering a hassle-free scaling solution.

## Availability

- **VM:** High availability can be achieved but requires additional configuration and maintenance.
- **App Service:** Designed for high availability and backed by Azure's SLAs.

## Workflow

- **VM:** Offers complete control over the environment, which can be advantageous for custom configurations.
- **App Service:** Simplifies deployment and management, ideal for streamlined workflows.

## Choice and Justification

I chose a VM for deploying the CMS app.

My decision was primarily influenced by cost considerations.

I believe that while VMs require more initial setup and ongoing maintenance, they can be more cost-effective in the long run, especially with proper optimization.

This approach suits my current requirements and budget constraints better than the App Service, which, while easier to manage and scale, comes at a higher cost.

# Assessing App Changes

For me to consider changing my decision from a VM to an App Service, several factors would need to change:

- **Increased Traffic and Scalability Needs:** If the app experiences significant growth in traffic, requiring more frequent scaling, the automatic scaling features of the App Service would become more appealing.
- **Maintenance Overhead:** Should the maintenance of the VM become too time-consuming or complex, the simplicity of the App Service would be a significant advantage.
- **Budget Flexibility:** If budget constraints were less of an issue, the higher cost of the App Service might be justifiable given its ease of use and built-in features.
- **Workflow Optimization:** A shift in workflow that favors quicker deployment and less hands-on management would make the App Service more attractive.
