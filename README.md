![logo](https://github.com/Guiiilhermee/booking-system/assets/127660583/d92580a5-8d66-49dd-be71-1549f2215be2)

# BLADES BARBER SHOP

The website provides a reservation system for barber services. It allows the customers to create an account and manage or delete their account, make haircut reservations profile and cancel or update their reservations. The application is built using Django framework, with several built-in modules and some custom code.

![photo of responsive screens](https://github.com/Guiiilhermee/booking-system/assets/127660583/56f9ffc7-07f2-4bcf-8ea4-fa27d34f0dfc)

### Site owner/administrator

The site owner or administrator will have full control over the system, as provided by Django's built-in administrator capabilities. The owner or administrator could:

- Access, update, and delete all users(customers) information.
- Access, update and delete any booking reservation.

### Customers/administrator

Customers are the users of the website which can register and create their own accounts.

![photos of the website](https://github.com/Guiiilhermee/booking-system/assets/127660583/d00427d6-7d39-4d9a-acc1-c659454119c1)
![make an appointment](https://github.com/Guiiilhermee/booking-system/assets/127660583/57fc600b-49d8-4297-a78e-ab17c1c29265)
![details of appointment](https://github.com/Guiiilhermee/booking-system/assets/127660583/f2ecf113-27a7-4fd3-8ebb-319dded16d9a)
![list of appointment](https://github.com/Guiiilhermee/booking-system/assets/127660583/304f999a-c862-45fa-b415-8898b2779db4)
![appointment deleted](https://github.com/Guiiilhermee/booking-system/assets/127660583/067210ca-ef33-4d59-83ba-1abf26ac93d0)

### Models

There are two models in this application: Services and Record(appointments).

- Service: It represents a service offered by the barber shop such beard trim, haircut, skin fade and haircut + beard trim. Each service has a price.

- Record: It represents an appointment which shows name, email, phone, date, time and service.  

### Forms

There are four forms: CreateUserForm, LoginForm, CreateRecordForm and UpdateRecordForm. 

- CreateUserForm: This form is used to create a new user account. The fields include , username, password and password confirmation.

- LoginForm: This form is used to login into the system with a valid username and password.

- CreateRecordForm: This form is used by administrators to add new records (appointments), it contains the fields name, email, phone, date, time and select the service.

- UpdateRecordForm: This form is the same as createRecordForm but it is to update the records (appointments), it also contains the fields name, email, phone, date, time and select the service.

### Views

There are several views handling the requests.

- HomeTemplateView: Handles requests to the homepage.
- register: Handles user registration request.
- my_login: Handles user logins.
- dashboard: Handles requests for displaying user's dashboard page.
- create_record: Handles record creation request.
- update_record: Handles updating records.
- singular_record: Handles showing single record details.
- delete_record: Handles deleting individual records.
- user_logout: Handles logging out from the user's account.

![register](https://github.com/Guiiilhermee/booking-system/assets/127660583/1f96f3c2-2ec8-45ed-bb9d-6d13e3f106fb)
![delete record](https://github.com/Guiiilhermee/booking-system/assets/127660583/06cecb3b-8c8e-49ac-9cac-b847c91bbc21)
![dashboard](https://github.com/Guiiilhermee/booking-system/assets/127660583/ce16e28b-da68-41e3-9fb4-ebc82b37ffa8)
![logout](https://github.com/Guiiilhermee/booking-system/assets/127660583/4e7c7f24-df64-4c82-8a6f-23ff740df7c3)
![updated](https://github.com/Guiiilhermee/booking-system/assets/127660583/84eef1fb-39f9-44d4-9764-faacb07dfd32)


### Error handling

Error 404 (Page Not Found) is handled by 404.html which can be found under templates/errors. It handles the users not registered.

### Bug fix

When I Debug the project to False, there was an issue with static files (CSS/JS) not being loaded properly. To resolve this problem I realized that I had to change cloudinary_storage to under django.contrib.staticfiles and DISABLE_COLLECTSTATIC 1 from VARS in Heroku, Then commit them out and deploy again to Heroku.

### Future features

- Enjoying the allauth library I can improve the login page with social account.   
- Create a profile for each user.
- Create time slots to the customers.
- Add more services.

### Validator and Testing

- PEP8 style guide and validated HTML and CSS code.
- Manual testing in differents browsers and devices.

![lighthouse](https://github.com/Guiiilhermee/booking-system/assets/127660583/68b988c9-5a10-46e6-a815-1fc327ec7af3)

### Unfixed Bugs

No unfixed bugs

### Deployment

The project was deployed using Code-Institute-Org/gitpod-full-template.

This project was deployed to Github pages using the following steps

- In the Github repository, navigate to the Settings tab, from the source section drop-down menu select the main branch.
- When the main branch has been selected, the page will automatically refesh with a detailed ribbon display to indicate the successful deployment.

Heroku:

- Create new heroku account or if you already have one create a new app.
- Add a name to your new app and choosethe region Europe then go to settings and add buildpacks python.
- Add in Config VAR. CLOUDINARY_URL, DATABASE_URL, HEROKU_HOSTNAME, HEROKU_POSTGRESQL_CYAN_URL, SECRET_KEY.
- Connect Heroku to GitHub/repository.
- Go to deploy

### Credits

- Code Institute for the deployment terminal.
- Elephant SQL
- Photos from Freepik uploaded to Cloudinary and downloaded to django.
- Youtube channel with tutorial videos.
