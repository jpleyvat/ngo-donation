# NGO Donations

## Development

### 1. Web Application.

The web application consists of an user authentication layer which gives access to an user to make identifiable donations and to a register of all donations made by that specific user if identified as regular user.

If identified as administrator user, the user will have access to all the Donations table. Administrator will also have access to Users and Type of Donations tables. This last two models are permitted to modify by an user identified as administrator. Donations table must not be editable.

Administrator and regular users will be both allowed to make donations. Upon completion an email confirmation and thanks will be sent to the email the user provides and the donation will be visible in his user donation management and in the administrator donations management.

It will be possible to make donations as a anonymous person person. In that case, there will be no user along the request and the person won't have access to any record of the donation other than the email sent (If an email not associated to an user is given at the moment of the donation. Otherwise the donation will be identified as made by the user who registered that email.)

NGO Donations application will be developed in Django.

We decided to use Django since the framework solves most of the problems we will face for developing an application that fulfills the required needs, it provides already a security layer needed since personal data will be handled by the application and will give us facilities at the time of deployment.

### 2. Database

We stablished the application will need 3 database models.

Users model will have user information such as first name, last name, email, password and role. All this fields are required. Role field distinguishes between administrator users and regular users. This will allow us to give access whether donations made by the user or to all donations it identified as a administrator user. This Table will also allow us to relate identifiable donations with the user who made them.

Donations model will have a register of the donations that have been made. Donations will have the following fields:

- Name identifies who made the donation. It will be Anonym by default if no user is identified at the moment of making the donation otherwise it will the name of the user will be assigned to this field or if the user wants to write a different name, this filed will take the name the user provides.
- Amount is be the amount of money donated in the local currency of the user (USD by default).
- Date is automatically set to the date the donation object is created, which will happen once payment is approved
- Donation Type identifies which cause is the user donating to.

All this fields are required.

Donations will have two optional fields.

- User is None by default and if donation is made by an identified user, it is set to that user instance through the user's id.
- Personal Information stores the PI of the person who is making the donation. If donation is made by an user, some of this data will be automatically filled (It can still be edited by the user.) If donation is made by an anonymous person, PI is set to as much PI the person provides.

Type of Donations Table will store all the different causes which people can make donations to. This table has the name of the Type of Donation which will be required. It will also have more information fields about the Type of Donation. This field will be optional.

For the database we will use MySQL.

We decided to use MySQL since we will need to maintain a relation between users and the donations they have made.

### 3. Donations

Donations will be made through Paypal API.

We decided to use Paypal since it already provides a complete API that we can implement for handling the payments and there is a library for python that allows us to integrate Paypal to our application smoothly and efficiently

## Testing

We will use a continuous integration approach during development, so we will implement unit testing, where we will build unit tests for all the services the application consists of. This tests will be constantly executing during the development and deployment of the application. This tests will be integrated with Jenkins during development and maintained on deployment stage to maintain reliability and stability of the application at all times.

## Deployment

The Django application will be deployed on a AWS EC2 instance/Docker container running in an AWS EC2 instance/Docker container running in AWS ECS.

We decided to use AWS EC2 instance/Docker container running in an AWS EC2 instance/Docker container running in AWS ECS because this will allow us to escalate easily and quickly the application when needed. Using docker will also solve many compatibility issues and make the application portability which might be useful in the future.

The MySQL database will be consumed from a AWS RDS service.

Both services will be connected to a private VPS which will be then accessed by the load balancer.

The application will be served through an AWS Load Balancer wich will be accessed through Route 53.
