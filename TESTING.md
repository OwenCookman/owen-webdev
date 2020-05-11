# Testing

The website was tested by [**Travis Continuous Integration**](https://travis-ci.org/) every time code was commited to GitHub


## Manual Testing

Manual testing was carried out on a Desktop computer

### Navbar
- Open the webpage in a new browser window
- Move mouse over each option and see that the text changes to a bright white
- Click the white link titles "Owen Cookman" and see that the page reloads
- Click the link titled "Home" and see that the page reloads
- Click the link titled "Porfolio" and see that the `Portfolio.html` page loads
- Click the link titled "Contact Me" and see that the `question.html` page loads
- Click the link titled "Login" and see that the `login.html` page loads
- Click the link titled "Register" and see that the `register.html` page loads
- Login through the login page
- Click the link titled "Order" and see that the `contact.html` page loads
- Click the link titled "logout" and see that the `index.html` page loads and you are logged out
- Right click on the page and select Inspect
- Select toggle device toolbar or press Ctrl+shift+M
- Set the device to responsive
- Move the slider in and out to see that the Navbar changes to have a burger icon at 991px
- Click the burger icon to see that the links are revealed


### Index Page
- Open the webpage in a new browser window
- Scroll down to the large button labelled "Hire Me!", click it and see that the Login page is loaded if you are not 
logged in or the `contact.html` page is loaded
- Return to the `index page` and scroll to the orange icons, see that clicking each icon opens a modal with information
about each title given to its corresponding icon, clicking the cross or outside of the modal closes it
- Scroll down to the "About Me" section and click "About Me", see that a collapse now opens containing text and the downward
pointing chevron has rotated to point up
- Click "About Me" again and see that the collapse closes and the upward facing chevron rotates to face downwards
- Right click on the page and select Inspect
- Select toggle device toolbar or press Ctrl+shift+M
- Set the device to responsive
- Move the slider in and out to see that the orange icons stack two by two at 767px and are replaced byan accordion with 
the headings of the icons at 575px
- Selecting the title "Targeted Design" see that the "Taylored Website" information closes and "Targeted Design" opens, work
your way down the titles seeing that when one opens the open one closes
- Select the open title to see that all information is closed

### Portfolio Page
- Open the webpage in a new browser window
- Select the link in the navbar titled "Portfolio" and see the `portfolio.html` page load
- See that the page is populated with an image accompanied by a title, GitHub repo link and some text
- Click the images to see a new tab open that loads the deployed website for each project
- Click the links titled "Github Repo" and see that a new tab opens with a link to the projects GitHub repositories
- Right click on the page and select Inspect
- Select toggle device toolbar or press Ctrl+shift+M
- Set the device to responsive
- Move the slider in and out to see that the images, title, link and text change to be stacked on top of each other at 991px

### User Registration
- Open the webpage in a new browser window
- Select the link in the navbar titled "Register" and see the `register.html` page load
- Enter an invalid email address and see a message that says "Please include an @ in the email address..."
- Enter a valid email address and see a message that says "Please fill in this field." appear on username
- Enter a Password that does not match the repeated password and see a message that says "passwords must match"
- Enter a valid email, username and matching passwords and see that you are redirected to the `index.html` page and 
the message "You have successfully registered" is showing at the top of the page

### User Login
- Open the webpage in a new browser window
- Select the link in the navbar titled "Login" and see the `login.html` page load
- Enter an invalid username or password and see the message "Your username or Password is incorrect"
- Enter a valid username and password and see that you are redirected to the `index.html` page and the message "You have 
succesfully logged in" is showing at the top of the page



### Editing an Order(Admin Panel)

### Paying a Deposit/Final Payment

### Viewing an Invoice

### Asking a Question

### Replying to a Question(Admin Panel)

### Editing a Question

### Deleting a Question

### Footer