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

### User Logout
- Open the webpage in a new browser window
- Select the link in the navbar titled "Login" and see the `login.html` page load
- Enter a valid username and password and see that you are redirected to the `index.html` page and the message "You have 
succesfully logged in" is showing at the top of the page
- Select the link in the navbar titled "Logout" and see that you are logged out and the message "You have been logged out 
successfully" is showing at the top of the page

### Creating an Order 
- Open the webpage in a new browser window
- Select the link in the navbar titled "Login" and see the `login.html` page load
- Enter a valid username and password and see that you are redirected to the `index.html` page and the message "You have 
succesfully logged in" is showing at the top of the page
- Select the link in the navbar titles "Order" and see  the `contact.html` page load
- Scroll to the bottom and click the button labelled "Send" and see that the page scrolls up with a cursor flashing in the 
first required field
- Fill in the required fields and click the button labelled "Send" and see the `profile.html` page load with the message
"Thank you, I will assess your order and be in touch via email with the cost and time it will take for your build" at the top 
of the page 

### Editing an Order(Admin Panel)
- After following the steps for Creating an Order
- Open the webpage in a new browser window
- Select the link in the navbar titled "Login" and see the `login.html` page load
- Enter a valid username and password for a Super User and see that you are redirected to the `index.html` page and the message 
"You have succesfully logged in" is showing at the top of the page
- Add to the end of the URL /admin and press enter, see that the Admin panel has loaded
- Select the link under the COMMS heading titled "orders"
- See that a link for a previously made order is loaded on to the page with the title of the business' name
- Select the order link and see that the details of the order are loaded on to the page
- Set a value to the "price" field and check the box for "Pay deposit"
- Click save and see the order page load with the message "The order X was changed successfully" where X is the name of the order

### Paying a Deposit/Final Payment
- After following the steps for Editing an Order
- Open the webpage in a new browser window
- Select the link in the navbar titled "Login" and see the `login.html` page load
- Enter a valid username and password for the user who created the order edited in Editing an Order and see that you are 
redirected to the `index.html` page and the message "You have succesfully logged in" is showing at the top of the page
- Click on the link in the navbar titled "Profile" and see the `profile.html` page load
- Click the "Your Orders" section and see the collapse open up to display the order details
- Right click on the page and select Inspect
- Select toggle device toolbar or press Ctrl+shift+M
- Set the device to responsive
- Move the slider in and out to see that the details stack two by two at 991px and vertically at 575px
- See that the price that was set is displayed under the heading "Total Cost" and there is a button labelled "Pay Deposit" or 
"Pay Final" under the heading "status"
- Click the "pay Deposit" button and see the `summary.html` page load
- See the order details rendered on the page and the sum under the heading "Total to Pay" is half of the value under the heading
"Total Cost"
- Click the button labelled "Print" and see a print preview of the page appear
- Close the print preview and click the button labelled "Make Payment". See the `payment.html` page load
- Enter invalid card details and see that a message appears stating that the details are invalid
- Enter the test card details Credit Card Number: 4242424242424242, CVV: any 3 digits, Expiry Month: any Month that hasn't passed
if using this year in Expiry Year and Expiry Year: this year if the Expiry month hasn't passed or any future year
- See that the `profile.html` page loads with the message "Payment taken successfully" is shown at the top
- Open the "Your Orders" section and see that under "status" it says "Deposit paid, awaiting completion" if you paid the deposit
or "Final payment made" if you paid the final payment

### Viewing an Invoice
- After following the steps for Editing an Order
- Open the webpage in a new browser window
- Select the link in the navbar titled "Login" and see the `login.html` page load
- Enter a valid username and password for the user who created the order edited in Editing an Order and see that you are 
redirected to the `index.html` page and the message "You have succesfully logged in" is showing at the top of the page
- Click on the link in the navbar titled "Profile" and see the `profile.html` page load
- Click the section titled "Invoice History" see that the collapse opens to show links labelled with the business name of the
order that was paid for in Paying a Deposit/Final Payment
- Click the link to see that the `invoice.html` page load
- See that the users details, the date of the invoice, a unique ID, the date work started, a description of what the payment was 
for, the brand and last 4 digits of the card used to pay the ammount paid and the remaining cost are displayed
- Right click on the page and select Inspect
- Select toggle device toolbar or press Ctrl+shift+M
- Set the device to responsive
- Move the slider in and out to see that the details stack on top of each other at 575px
- Click the button labelled "Print" and see a print preview of the page appear


### Asking a Question
- Open the webpage in a new browser window
- Select the link in the navbar titled "Contact Me" or the link in the footer and see the `question.html` page load
- Click the button labelled "Send" and see the message "Please fill in this field" appear on the Name input
- Fill in the Name field and press "Send", see that the message appears on the Email input
- Fill in the Email field and press "Send", see that the message appears on the Message field
- Fill in the form and press "Send", see that you are redirected to the `index.html` page with the message "Thank you for your 
message, I will get back to you shortly" at the top of the page
- Select the link in the navbar titled "Login" and see the `login.html` page load
- Enter a valid username and password and see that you are redirected to the `index.html` page and the message "You have 
succesfully logged in" is showing at the top of the page
- Select the link in the navbar titled "Contact Me" or the link in the footer and see the `question.html` page load
- Fill in the form and press "Send", see that you are redirected to the `profile.html` page with the message "Thank you for your 
message, I will get back to you shortly" at the top of the page
- Click on the section titled "Your Questions" and see the collapse open to reveal the question you had asked

### Replying to a Question(Admin Panel)
- Open the webpage in a new browser window
- Select the link in the navbar titled "Login" and see the `login.html` page load
- Enter a valid username and password for a Super User and see that you are redirected to the `index.html` page and the message 
"You have succesfully logged in" is showing at the top of the page
- Add to the end of the URL /admin and press enter, see that the Admin panel has loaded
- Select the link labelled "questions" under the section titled "COMMS" and see that a list of links labelled with different 
Names is displayed
- Select the Name who's question you would like to reply to and see the details of the question displayed
- Type your answer in to the box labelled Answer
- Select the button labelled "Save" and see the page of Names load with the message "The question “X” was changed successfully." 
where X is the name

### Editing a Question
- Open the webpage in a new browser window
- Select the link in the navbar titled "Login" and see the `login.html` page load
- Enter a valid username and password for a user who has asked a question and see that you are redirected to 
the `index.html` page and the message "You have succesfully logged in" is showing at the top of the page
- Select the link in the navbar titled "Profile" or the link in the footer and see the `profile.html` page load
- Click on the section titled "Your Questions" and see the collapse open to reveal the question you had asked
- Click the button labelled "Edit" and see that the `question.html` page loads with the fields filled in with the
details of the question
- Make the changes you would like to make and click "Send"
- see that you are redirected to the `profile.html` page with the message "Question edited successfully" displaying at the top
of the page
- Click on the section titled "Your Questions" and see the collapse open to reveal the question you had asked shown with the 
changes that you made

### Deleting a Question

### Footer