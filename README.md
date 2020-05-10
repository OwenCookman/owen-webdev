[Owen Cookman Web Developer](https://owen-cookman-web-dev.herokuapp.com/)
======
[![Build Status](https://travis-ci.com/OwenCookman/owen-webdev.svg?branch=master)](https://travis-ci.com/OwenCookman/owen-webdev)

The webpage was created to advertise myself as a web developer, showcasing my portfolio of previous projects 
which should be regularly updated as more projects are finished, giving those who visit the website an introduction to 
myself, the work I have done, a way to contact me for consultations and also a way to hire and pay me as a freelance 
developer.

## UX

The website is aimed at potential clients who would like to hire me as a developer.

### User Stories

As a visitor I expect:
1. To read about the developer and learn about their background
2. To see the developers portfolio of work to understand what they are capable of
3. To be able to contact the developer with any questions that I may have
4. To navigate the website easily
5. The information to be laid out in an easy to view format

As a User I expect:
1. To read about the developer and learn about their background
2. To see the developers portfolio of work to understand what they are capable of
3. To be able to contact the developer with any questions that I may have
4. To navigate the website easily
5. The information to be laid out in an easy to view format
6. To be able to hire the developer
7. To be able to see what options are available to me
8. To be able to select the options that I like
9. To be able to pay the developer for their services
10. To be able to keep in contact with the developer during the development process
11. To be able to provide feedback to the developer on their services

As the Developer I expect:
1. Visitors to my website to be able to learn about my background
2. To showcase my portfolio of work where possible to show visitors what I can offer
3. Visitors to be able to sign up to my website and become users
4. Visitors to be able to contact me with any queries they may have
5. Users to be able to see what packages I have on offer
6. Users to be able to select which package they want
7. Users to be able to give a description of their business and what their expectations are
8. To be able to keep constant contact with users who have hired me
9. Users to be able to pay me for my services
10. Users to be able to provide feedback where possible

### Styling Choices

#### Colours
I wanted to aim for a **neutral** colour palette with this website as my clients could be looking to build websites with 
a whole range of **themes**. This led me to look at neutral colour **groups**. I settled on a dark navy blue for the **nav** and 
**footer** elements, this would **seperate** them from other sections of the page. I decided to keep the page **background** as **white**
while content would appear on an **opaque field**. This allowed content to be **stacked** within itself making the field around 
the inner content **darker** which would seperate **generated** content even though they are generated in the same container
for example when a user asks multiple questions.

#### Fonts
I decided to go with the **Inria Sans** font as it still looked **professional** and neat but also **different** from what is seen
on a lot of other web pages, I noticed that this **paired** well with the **Roboto** font so I decided that any **titles** or **headers**
would be styled with **Inria Sans** and any other blocks of text would use **Roboto**. This further breaks content up and keeps 
the page looking **interesting**.

#### Favicon
The favicon was taken from [**PNG Fuel**](https://www.pngfuel.com/free-png/fdyur) I was looking for a **simple** icon that
would explaine exactly what the website **involves**, the **laptop** with the </> symbol for **code** was perfect in showing that I 
am a **developer**. 

### Wireframes 

Please click [here](wireframes) to view my first draft Wireframes, these were originally made using Balsamiq Mock-ups.

#### Changes
The **'About Me'** page and **'What I do'** page were later combined on to the **index** page as this would be the landing point where
this information could be displayed to **sell** myself as a **developer** rather than having two small seperate pages.

## Features

### Theme

The original Theme was taken from the Bootswatch themes library, the theme Sandstone was used and then styled with CSS to 
customize it further such as the fonts used and the changes made to the navbar, The buttons provided were kept the same
as the colours worked well with my palette but the font used in the button was changed to match the other text on the page.

### navbar

### Index Page/Introduction

### Portfolio

### User Authentication

### User Profile

### Order Page

### Contact Me Page


## Possible Features To Implement
- A more detailed contact form using check boxes that could give an estimated cost of the website build to the client
- A built in chat system allowing text communication to be handled completely on the website for example the chat system used
by Tutor support at ci
- The content on the portfolio page to be rendered from the database, with new entries uploaded from the admin pannel
- Email notifications when visitors/users ask a question and invoices/confirmations sent to users email

## Technologies Used

### Languages
- This project uses **HTML**, **CSS**, **JavaScript** and **Python** programming languages
### Frameworks & Libraries
-[**Django 3.0.4**](https://www.djangoproject.com/)
- [**Stripe**](https://stripe.com/gb)
- [**Bootstrap**](https://getbootstrap.com/)
- [**FontAwesome**](https://fontawesome.com/)
- [**Google Fonts**](https://fonts.google.com/)
- [**Popper.js**](https://popper.js.org/)
### Tools
- [**GitPod**](https://www.gitpod.io/) was used as the development IDE
- this projects wireframes were created on [**Balsamiq**](https://balsamiq.com/)
- The CSS code was validated using the [**W3C Markup Validation Service**](https://validator.w3.org/) website
- The build was tested with [**Travis Continuous Integration**](https://travis-ci.org/)
### Databases
- An SQLite database was used in development
- A PostgreSQL database is used in deployment


## Testing

To view the testing carried out on this project please click [here](TESTING.md) for my separate testing file