# Frisa Booking

![AmIResponsive image of Frisa Booking](doc/amiresponsive.webp)

## Introduction

The project is to build a website where you as a user can book a space in a local art studio. If the user doesn't visit the website with the goal to book a workshop right away, the website should work as an inspiration.

## Table of Contents

- [Studio Booker](#studiobooker)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [User Experience](#user-experience)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
    - [User Stories](#user-stories)
      - [Epic 1 - User account creation process](#epic-1---user-account-creation-process)
      - [Epic 2 - Development of a studio booking system](#epic-2---development-of-a-course-booking-system)
      - [Epic 3 - Development of a contact form](#epic-3---development-of-a-contact-form)
      - [Epic 4 - Enhancing website aesthetics](#epic-4---enhancing-website-aesthetics)
      - [Epic 5 - Employee workshop news feed](#epic-5---employee-workshop-news-feed)
  - [Design](#design)
    - [Color Scheme](#color-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
    - [Wireframes](#wireframes)
      - [Index page](#index-page)
      - [About page](#about-page)
      - [Booking page](#booking-page)
      - [My bookings page](#my-bookings-page)
      - [Success page](#success-page)
      - [Edit booking page](#edit-booking-page)
      - [Sign up page](#sign-up-page)
      - [Sign in page](#sign-in-page)
      - [Sign out page](#sign-out-page)
      - [404 page](#404-page)
      - [500 page](#500-page)
    - [Entity Relationship Diagram - ERD](#entity-relationship-diagram---erd)
  - [Features](#features)
    - [Header](#header)
      - [Navigation bar](#navigation-bar)
      - [Navigation bar (as a logged in user)](#navigation-bar-as-a-logged-in-user)
      - [Navigation bar (as a staff member or superuser)](#navigation-bar-as-a-staff-member-or-superuser)
    - [Index page](#index-page-1)
      - [Hero image](#hero-image)
      - [Welcome text](#welcome-text)
      - [Member benefits](#member-benefits)
      - [Sign up button](#sign-up-button)
      - [Carousel](#carousel)
    - [About page](#about-page-1)
      - [Profile image](#profile-image)
      - [About text](#about-text)
      - [Contact form](#contact-form)
      - [Contact form response](#contact-form-response)
    - [Booking page](#booking-page-1)
      - [Workshop presentation](#workshop-presentation)
      - [Workshop booking](#workshop-booking)
      - [Booking pagination](#booking-pagination)
      - [Confirm booking modal](#confirm-booking-modal)
      - [Double booked modal](#double-booked-modal)
    - [Success page](#success-page-1)
      - [Confirmation text](#confirmation-text)
      - [Navigation buttons](#navigation-buttons)
    - [My bookings page](#my-bookings-page-1)
      - [No bookings - text](#no-bookings---text)
      - [No bookings - button](#no-bookings---button)
      - [Active bookings - text](#active-bookings---text)
      - [Active bookings - booked workshops](#active-bookings---booked-workshops)
      - [Active bookings pagination](#active-bookings-pagination)
      - [Confirm cancellation modal](#confirm-cancellation-modal)
    - [Edit booking page](#edit-booking-page-1)
      - [Available workshops](#available-workshops)
      - [Available workshops pagination](#available-workshops-pagination)
      - [Confirm workshop change modal](#confirm-workshop-change-modal)
    - [News page](#news-page)
    - [Sign up page](#sign-up-page-1)
    - [Sign in page](#sign-in-page-1)
    - [Sign out page](#sign-out-page-1)
    - [404 page](#404-page-1)
      - [404 page text](#404-page-text)
      - [404 page button](#404-page-button)
    - [500 page](#500-page-1)
      - [500 page text](#500-page-text)
      - [500 page tips](#500-page-tips)
    - [Footer](#footer)
  - [Features to be Added](#features-to-be-added)
  - [Testing](#testing)
    - [Validation of Code](#validation-of-code)
      - [HTML](#html)
      - [CSS](#css)
      - [JavaScript](#javascript)
      - [Python](#python)
    - [Lighthouse](#lighthouse)
      - [Desktop](#desktop)
      - [Mobile](#mobile)
    - [Wave Webaim - accessibility testing](#wave-webaim---accessibility-testing)
      - [Index page](#index-page-2)
      - [About page](#about-page-2)
      - [Booking page](#booking-page-2)
    - [Contrast Grid](#contrast-grid)
    - [Automated Testing](#automated-testing)
      - [About](#about)
      - [Booking](#booking)
      - [News](#news)
    - [Manual Testing](#manual-testing)
      - [Navigation bar](#navigation-bar-1)
      - [Index page](#index-page-3)
      - [About page](#about-page-3)
      - [Booking page](#booking-page-3)
      - [Success page](#success-page-2)
      - [My bookings page](#my-bookings-page-2)
      - [Edit booking page](#edit-booking-page-2)
      - [News page](#news-page-1)
      - [Sign up page](#sign-up-page-2)
      - [Sign in page](#sign-in-page-2)
      - [Sign out page](#sign-out-page-2)
      - [404 page](#404-page-2)
      - [500 page](#500-page-2)
      - [Footer](#footer-1)
    - [Bugs](#bugs)
  - [Technologies Used](#technologies-used)
  - [Deployment](#deployment)
    - [Fork repository in GitHub](#fork-repository-in-github)
    - [Clone repository in GitHub](#clone-repository-in-github)
    - [Deployment to Heroku](#deployment-to-heroku)
  - [Credits](#credits)
    - [Libraries used](#libraries-used)
    - [Used resources](#used-resources)
    - [Images](#images)
  - [Acknowledgements](#acknowledgements)

## User Experience

### User Goals

One of the user goals is to be able to book __________. The user should also have a smooth experience with full CRUD (Create, Read, Update and Delete) accessibility to their bookings. The goal is also to view already created projects and to inspire the user.

### Site Owner Goals

The site owner goal is to get more bookings to the hosted workshops.

### User Stories

For the project, five different Epics were created. To them, a total of ____ user stories were created. To view all user stories, they are viewable at the [Projects board](). All user stories were assigned one of the following classes; Must have, Should have, Could have or Won't have. Each of the user stories were also assigned points depending on how much time they were estimated to take.

| Class | Points | Percentage of total points |
| -------------- | --------- | --------------- |
| Must have |  p |  % |
| Should have |  p |  % |
| Could have |  p |  % |
| Won't have |  p |  % |

The following user stories were completed within the first release of Studio Booker. To view the Won't have, they are listed in the [Project board]().

#### Epic 1 - User account creation process

As a site owner, I would like to enable a seamless, secure, and user-friendly account creation process for new users, so that they can efficiently transition from sign-up to verification and initial login, ultimately engaging with the platform's features smoothly.

**User Story - Accessing the sign-up page**

As a site user I can easily find and access the sign-up page from the homepage so that I can create an account without confusion or unnecessary delays

- Acceptance Criteria 1  
Given that I am a not signed in user  
When I visit the page  
Then a visible and clearly labeled "Sign Up" button is present on the homepage  
- Acceptance Criteria 2  
Given that I am a not signed in user  
When clicking the "Sign Up" button  
Then it navigates the user to the sign-up form  

**User Story - Filling out the sign-up form**

As a site user I can enter my personal details into a sign-up form so that I can register for a new account

- Acceptance Criteria 1  
Given the user isn't signed in  
When the user is filling out the sign up form  
That the form includes fields for necessary information (e.g., email, password, confirmation of password)  
- Acceptance Criteria 2  
Given the user isn't signed in  
When the user is filling out the sign up form  
That the form has input validation (e.g., email format)

#### Epic 2 - Development of a course booking system

As a site owner I would like to have a comprehensive, user-friendly booking system, so that users can effortlessly view, create, modify, and cancel bookings for various courses so that the user easy can book courses.

**User Story - Viewing available courses**

As a registered user I can easily view all available courses so that I can decide which courses to book based on my interests and schedule

- Acceptance Criteria 1  
Given as a site visitor  
When the booking page is visited  
Then a list of courses is available  
- Acceptance Criteria 2  
Given as a site visitor  
When the booking page is visited  
Then course listing includes essential details such as course title, description, dates, and availability  

**User Story - Creating a new booking**

As a registered user I can book a course so that I can secure my spot in courses I'm interested in attending

- Acceptance Criteria 1  
Given that the user is signed in  
When the user is visiting the booking page  
Then a clear "Book Now" button is available for courses with available spots  
- Acceptance Criteria 2
Given that the user is signed in  
When the user is visiting the booking page  
Then the booking process collects necessary user information and confirms the booking  

**User Story - Viewing my bookings**

As a registered user I can view a list of my current course bookings so that I can manage my schedule and review the courses I'm enrolled in

- Acceptance Criteria 1  
Given the user has enrolled at a course  
When the user visit the personal dashboard  
Then the user can view their bookings  
- Acceptance Criteria 2  
Given the user has enrolled at a course  
When the user visit the personal dashboard  
Then the user can view each each booking entry including course details and the booked date  

**User Story - Modifying an existing booking**

As a registered user I can change the date or details of my existing course bookings so that I can adjust my schedule

- Acceptance Criteria 1  
Given the user has an existing booking  
When the user is signed in  
Then the user can modify bookings in the user's booking dashboard  

**User Story - Cancelling a booking**

As a registered user I can cancel a booking if I can no longer attend so that I can manage my commitments and possibly allow others to book the now-available spot

- Acceptance Criteria 1  
Given the user has a booked course  
When the user visit their booking dashboard  
Then the user can cancel their booking  
- Acceptance Criteria 2  
Given the user has a booked course  
When the user cancel their booking  
Then the user get a confirmation in form of a message at the site  

**User Story - Implement modal pop-up confirmations for booking and booking changes**

As a site user I can receive immediate, clear confirmation requests in the form of modal pop-ups whenever I attempt to make any changes to my bookings so that instantly understand the impact of my actions and confirm my intentions in a more interactive and user-friendly manner, avoiding the passive nature of Django's built-in messages

- Acceptance Criteria 1  
Given a user is on the booking or booking modification page  
When the user initiates a new booking or change to an existing booking  
Then a modal pop-up should immediately appear, confirming the booking or change  
- Acceptance Criteria 2  
Given a modal pop-up is displayed to the user  
When the user confirms the proposed action by clicking the "Confirm" button  
Then the booking should be updated accordingly in the system, and the changes will be visible immediately  
- Acceptance Criteria 3  
Given a modal pop-up is displayed to the user  
When the user clicks the "Cancel" button to abort the proposed change  
Then the modal should close without making any modifications to the booking, and the user should remain on the page without any further action taken  

#### Epic 3 - Development of a contact form

As a site owner I can have a user-friendly contact form so that visitors can easily send messages, inquiries, or feedback directly through our website, enhancing communication and engagement

**User Story - Accessing the contact form**

As a site user I can easily find and access the contact form from any page on the website so that I can contact the website owner without hassle

- Acceptance Criteria 1  
Given the user is anywhere at the website  
When the user wants to contact the site owner  
Then a clear and accessible link to the contact form is available on every page, either in the navigation menu or footer  
- Acceptance Criteria 2  
Given the user is anywhere at the website  
When the user tries to reach the contact form  
Then the contact form page loads efficiently and is mobile-responsive  

**User Story - Submitting a message**

As a site user I can submit messages using the contact form so that I can communicate my inquiries, suggestions, or feedback

- Acceptance Criteria 1  
Given the user has any questions  
When the user is trying to use the contact form  
Then the form includes fields for name, email and message  
- Acceptance Criteria 2  
Given the user has any questions  
When the user is trying to use the contact form  
Then there is validation for each field to ensure the information is entered correctly  
- Acceptance Criteria 3  
Given the user has any questions  
When the user is trying to use the contact form  
Then a clear "Submit" button sends the message and provides a confirmation to the user that it has been sent  

**User Story - Receive confirmation after sending contact form**

As a site user I can receive immediate confirmation that my message has been sent successfully when I submit the contact form so that I am assured my message has been received and will be addressed

- Acceptance Criteria 1  
Given I am a website visitor on the contact page  
When I fill out the contact form with my information and submit it  
Then I should see a confirmation message on the website indicating that my message has been sent successfully  

#### Epic 4 - Enhancing website aesthetics

As a website owner I would like to enhance the visual appeal and user experience of the website so that visitors are more engaged, find the website more trustworthy, and are encouraged to sign up for courses due to an attractive and professional presentation

**User Story - Implementing a responsive design**

As a site user I can easily navigate and view content so that I can use any device, whether it's a desktop, tablet, or smartphone, ensuring a seamless experience

- Acceptance Criteria 1  
Given the user is visiting the site  
When the user is using different devices  
Then the website automatically adjusts its layout based on the screen size and orientation  
- Acceptance Criteria 2  
Given the user is visiting the site  
When the user is using different devices  
Then all elements, including text, images, and buttons, are easily readable and accessible on various devices  
- Acceptance Criteria 3  
Given the user is visiting the site  
When the user is using different devices  
Then navigation menus are optimized for touch interactions on mobile devices  

**User Story - Uploading high-quality images for courses**

As a site owner I can upload high-quality images for each course so that visitors are visually attracted to the courses and can make informed decisions to sign up, enhancing course appeal through professional and engaging imagery.

- Acceptance Criteria 1  
Given the site owner have high-quality images  
When the site owner wants to draw attention to the different courses  
Then the website provides an interface for administrators to upload, edit, and associate images with specific courses  
- Acceptance Criteria 2  
Given the site owner have high-quality images  
When the site owner wants to draw attention to the different courses  
Then the uploaded images are automatically resized and optimized for web use without compromising quality  
- Acceptance Criteria 3  
Given the site owner have high-quality images  
When the site owner wants to draw attention to the different courses  
Then each course section displays its associated image prominently, with clear, high-resolution visuals  

**User Story - Utilizing modern, attractive fonts and color scheme**

As a site user I can visit the website with modern, attractive fonts and a cohesive color scheme so that eading and interacting with the site is a pleasant experience, contributing to the overall aesthetic appeal and professionalism

- Acceptance Criteria 1  
Given the user doesn't only use screen reader  
When the user visits the website  
Then the website adopts a consistent set of fonts that are easy to read and visually appealing  
- Acceptance Criteria 2  
Given the user doesn't only use screen reader  
When the user visits the website  
Then a color scheme is chosen that reflects the brand and enhances readability, with sufficient contrast between text and background colors  
- Acceptance Criteria 3  
Given the user doesn't only use screen reader  
When the user visits the website  
Then text styling is consistent throughout the website  

**User Story - Playful and engaging text content**

As a website owner I can incorporate text content throughout my website that is fun, engaging, and easygoing so that visitors can experience my playful side and enjoy a more relatable and memorable visit to my site

- Acceptance criteria 1  
Given I am reading the text content on the website  
When I engage with any piece of content (such as about us, services, or blog posts)  
Then the text should feel like a conversation with a friend, using casual language, jokes, or puns where appropriate, making the reading experience enjoyable and relaxed  

#### Epic 5 - Employee workshop news feed

As a site user (employee) I can access the employee workshop news feed so that I can stay informed about workshops and learn from my colleagues' experiences

**User Story - Submitting workshop stories**

As a site user (employee) I can submit stories about the workshops I have held so that share my experiences and insights with my colleagues.

- Acceptance criteria 1  
Given the user is logged in and has held a workshop  
When the user navigates to the employees page and fills in the story submission form with details about the workshop (title, content, etc.) and submits it  
Then the story is published to the news feed  
- Acceptance criteria 2  
Given the user has filled in the submission form but left some mandatory fields empty  
When the user attempts to submit the form  
Then an error message is displayed, and the submission is not processed until all mandatory fields are filled  

**User Story - Reading workshop stories**

As a site user (employee) I can read stories about workshops submitted by my colleagues so that I can learn from their experiences

- Acceptance Criteria 1  
Given the user is logged in  
When the user navigates to the news feed  
Then the user can see a list of published workshop stories  

**User Story - Deleting own post**

As a site user (employeer) I can delete my own posts on the employee workshop news feed so that I can remove content that I no longer wish to share or that has become outdated

- Acceptance Criteria 1  
Given the user is logged in and viewing their own post on the employee workshop news feed  
When the user selects the option to delete their post  
Then the system prompts the user to confirm the deletion to prevent accidental removal  
- Acceptance Criteria 2  
Given the user confirms the deletion of their post  
When the deletion process is initiated  
Then the post is permanently removed from the news feed, and the user receives a confirmation message that their post has been successfully deleted  

## Design

The design is set to be modern but easy to read. It should draw the attention to the images which . 

### Color Scheme

The color scheme is set to feel modern and harmonize with the hero image. Any bright colors in the scheme were avoided to not draw any attention from the images at the website. The colors are reused on all pages to make every page feel familiar and to enhance the feeling that the website is a unit. 

### Typography

The typography was chosen to have a modern touch. It was chosen to feel easygoing and fun, but at the same time easy to read. The text was designed to incorporate some spacing, ensuring it doesn't appear as a dense block of text upon opening a page. The written communication across the website adopts a playful tone to foster a friendly atmosphere. Emojis were added to make the tone more playful and friendly.  

### Imagery

All the images are chosen to inspire the website users. The images should give a warm feeling through their content and warm tone. The images have been designed with a playful and dynamic excerpt to encourage user engagement and increase sign-ups for the workshops. The objects on the images are things that has been made by the leader of the workshops. In other words, they are objects that you can create at the workshops!

### Wireframes

#### Index page

![Wireframe of index page]()

#### About page

![Wireframe of about page]()

#### Booking page

![Wireframe of booking page]()

#### My bookings page

![Wireframe of my bookings page]()

#### Success page

![Wireframe of success page]()

#### Edit booking page

![Wireframe of edit booking page]()

#### Sign up page

![Wireframe of sign up page]()

#### Sign in page

![Wireframe of sign in page]()

#### Sign out page

![Wireframe of sign out page]()

#### 404 page

![Wireframe of 404 page]()

#### 500 page

![Wireframe of 500 page]()

### Entity Relationship Diagram - ERD

Three different models were used in the making of the website.

![ERD of Booking Model](doc/erd-booking.webp)

![ERD of Course Model](doc/erd-course.webp)

![ERD of CourseSession Model](doc/erd-coursesession.webp)

## Features

### Header

#### Navigation bar

![Navigation bar as a not logged in user]()

.

#### Navigation bar (as a logged in user)

![Navigation bar as a logged in user]()

. 

#### Navigation bar (as a staff member or superuser)

![Navigation bar as a staff member or superuser]()

.

### Index page

#### Hero image

![Hero image at index page]()

.

#### Welcome text

![Welcome text at index page]()

.

#### Member benefits

![Benefits of becoming a member]()

. 

#### Sign up button

![Sign up button below member benefits]()

If the user is visiting the index page without being signed in, there is a sign up button below the member benefits. This is to make it easy for the user to sign up when they have read the fantastic benefits. 

#### Carousel

![Carousel of images]()

At the bottom of the index page, a carousel with images are located. This carousel is there to present several more objects that can be created at the workshops. Their goal is to inspire users and increase their interest in registering for the workshops. The start image is an image with a text on it to get the user to start looking at the images.

### About page

#### Profile image

![Profile image at the about page](d)

. 

#### About text

![A text about the owner and founder of ]()

.

#### Contact form

![The contact form at the about page]()

.

#### Contact form response

![The response after submitting the contact form]()

.

### Booking page

#### Studio Space Presentation

![The three different workshops are presented]()

The three different .

#### Space booking

![The booking section where the user can select which session they are interested in](doc/workshop-booking.webp)

.

#### Booking pagination

![Pagination at booking page]()

.

#### Confirm booking modal

![Confirmation modal after a booking button in pressed]()

.

#### Double booked modal

![Modal to show that the user already has a booking at the chosen studio space]()

A double booking modal is triggered when the user tries to book a .

### Success page

#### Confirmation text

![Confirmation text after a successful booking]()

After a successful booking, a text that confirm the booking appears.

#### Navigation buttons

![Three navigation buttons; "View my bookings", "Home" and "Book another space"]()

Under the confirmation text, three navigation buttons are visible; "View my bookings", "Home" and "Book another workshop". On smaller devices, only "View my bookings" and "Book another workshop" are visible. These buttons are there to make the user to stay at the website after a successful booking.

### My bookings page

#### No bookings - text

![The text on my booking page explains there is no bookings]()

When the user doesn't have any active bookings, a text informs the user about it. The text informs the user where they can find the booking page.

#### No bookings - button

![Button to direct the user to the booking page]()

.

#### Active bookings - text

![Text to notice the user that they have at least one active booking]()

When the user has at least one booking, the user gets a text that informs that all their booked sessions are presented below. The text is also supposed to get the user to have a small giggle and get excited for upcoming workshops.

#### Active bookings - booked workshops

![The user bookings are presented]()

The user bookings are presented so that the workshop that is next in time appears first. Each booked workshop card has an Edit button and a Cancel button. When the Edit button is pressed, the user gets directed to the edit booking page. When the Cancel button is pressed, a confirmation modal is triggered. These two buttons allows the user to edit and delete the booked session if the user has to change their plans.

#### Active bookings pagination

![My bookings pagination](doc/my-bookings-pagination.webp)

If the user has more than four active bookings, a pagination appears below the active bookings. This is to enhance the user experience, to make it easier for the user to see their active bookings.

#### Confirm cancellation modal

![Modal that the user gets to assure that they want to cancel their booking](doc/confirm-delete.webp)

When the user presses the Cancel button in their active bookings, a confirm cancellation modal is triggered. This is to make sure the user didn't press Cancel by mistake. The Confirm button in the modal is red to mark that if you press it, something that is irreversible will happen.

### Edit booking page

#### Available Spaces

![All available workshops presented as booking buttons](doc/available-workshops.webp)

All available workshops are presented in a similar way as on the booking page. The title of the workshop, date, time and available spots are presented. The similarity should make the user recognize the how to book a workshop session. When the user clicks the workshop they want to change their booking to, a confirmation modal is triggered.

#### Available Spaces Pagination

![Available Spaces Pagination]()

If there are more than eight available workshops to select from, pagination appears. This is to enhance the user experience, to avoid scrolling through a wall of available workshops.

#### Confirm workshop change modal

![Confirmation modal to ensure the user wants to change their workshop booking](doc/confirm-edit.webp)

The confirmation modal ensures that the user wants to edit their booking to the selected workshop session. This to avoid the user editing their booking to a session they didn't want to book. The text is written in a way that should enhance the user's feeling that this is a friendly and fun website.

### News page

![News page, only visible for staff members and superusers](doc/news-page.webp)

The news page is only visible for staff members and superusers. Through the admin panel all staff members and superusers can write news of what happened at their latest workshop. The name of the workshops are located below the header. The name of the member who has written it and when it is published are located at the bottom of the section.

### Sign up page

![Sign up page with fields for email, username, password and password again](doc/sign-up.webp)

The sign up page have fields where the user is required to fill out email, username, password and password again. This to make sure the user doesn't get a typo in the password and to ensure the user register a way to contact them.

### Sign in page

![Sign in page with fields for email and password](doc/sign-in.webp)

The sign in page allows the user who already has an account to sign in. This to make the user experience smoother where they don't have to fill out their email every time they want to make a booking. It is also an advantage that the user can see all their bookings.

### Sign out page

![Sign out page with a confirmation button](doc/sign-out.webp)

The sign out page allows the user to sign out to ensure no one else can edit the users booking. The sign out button ensures the user really wanted to sign out and didn't press on Sign out by mistake.

### 404 page

#### 404 page text

![Text provided when a 404 page is rendered](doc/404-text.webp)

The text explains to the user in a fun way that the page they are looking for doesn't exist. It points the user in the direction of heading back to the homepage to give it a new try.

#### 404 page button

![Button which takes the user to the homepage](doc/404-button.webp)

The button below the 404 text directs the user back to the homepage. This allows the user to give it a new shot to find the page they were looking for.

### 500 page

#### 500 page text

![Screenshot of the text at the 500 page](doc/500-text.webp)

The text at the 500 page explains to the user that the server isn't working as intended. This is to make sure the user knows what is happening.

#### 500 page tips

![The tips of what to do when a 500 page is rendered](doc/500-tips.webp)

The tips suggests to the user what they can do; refresh the page, go back to the homepage or send the website owner an email. The suggestion about going back to the homepage is provided with a link to the homepage. The suggestion about sending an email is provided with a link to the contact form.

### Footer

![Footer with developers name and year to the left and links to the Contact form and connecting Facebook, Instagram and Pinterest accounts](doc/footer.webp)

To the left, the developers name is to tell the world who the brain behind the website is. To the right, four symbols represent what they link to. The first, the pen, links the user to the Contact form at the about page. The second, Facebook icon, links the user to Facebook in a new tab. The third, Instagram icon, links the user to Instagram in a new tab. The fourth, Pinterest icon, links to Pinterest in a new tab.

## Features to be Added

Several features can be added in the future.

- Select if you as a user want to have a notification a couple of days before it is time for the workshop.
- Be able to select how many spots you want to book at each workshop.
- Include an online shop were you could buy some upcycled things created by the owner.
- Implement a review section where the user who has been at the workshops can write reviews.
- Sign in with Social media account or Google credentials.
- Captcha verification when the user is signing up with email address.
- Guidance when a user sign in for the first time.

## Testing

### Validation of Code

#### HTML

![Screenshot of HTML validation of index page](doc/index-html-valid.webp)

All the pages were tested at the [W3C Markup Validation Service](https://validator.w3.org/). The index page validation is presented above, all the other validations are linked below.

- [About page](doc/about-html-valid.webp)
- [Booking page](doc/booking-html-valid.webp)
- [My bookings](doc/my-bookings-html-valid.webp)
- [News page](doc/news-html-valid.webp)
- [Edit booking](doc/edit-booking-html-valid.webp)
- [Success page](doc/success-html-valid.webp)
- [404 page](doc/404-html-valid.webp)
- [500 page](doc/500-page-html-valid.webp)

#### CSS

![Screenshot of CSS validation](doc/css-valid.webp)

The CSS code was tested at [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). It resulted without any errors but with one warning. The warning was "Imported style sheets are not checked in direct input and file upload modes" which refers to the fonts which are imported from Google fonts.

#### JavaScript

All three JavaScript files were validated through [JSHint](https://jshint.com/). The validation rendered without errors. In two of the files, Booking and Edit Booking, one undefined variable was discovered. This undefined variable was bootstrap. This variable originates from the Bootstrap framework and is thus declared in its documentation.

**Booking page**

![JavaScript validation of Booking page](doc/js-valid-booking.webp)

**Edit booking page**

![JavaScript validation of Edit booking](doc/js-valid-edit.webp)

**Delete booking**

![JavaScript validation of Delete booking](doc/js-valid-delete.webp)

#### Python

All Python files have been validated through [CI Python Linter](https://pep8ci.herokuapp.com/) to make sure the code meets the standards of PEP8. The validation resulted without errors.

**Bookings - views.py**

![Python validation of views.py in bookings](doc/pep8-booking-views.webp)

**About - views.py**

![Python validation of views.py in about](doc/pep8-about-views.webp)

**News - views.py**

![Python validation of views.py in news](doc/pep8-news-views.webp)

- [Python validation of models.py in bookings](doc/pep8-booking-models.webp)
- [Python validation of admin.py in news](doc/pep8-news-admin.webp)
- [Python validation of models.py in news](doc/pep8-news-models.webp)

### Lighthouse

Tests in Lighthouse were performed for both desktop and mobile.

#### Desktop

![Lighthouse test for desktop](doc/lighthouse-desktop.webp)

The test for desktop resulted in 98 in both performance and accessibility. It also resulted in 100 in both best practice and SEO.

#### Mobile

![Lighthouse test for mobile](doc/lighthouse-mobile.webp)

The test for mobile resulted in 91 in performance and the same score for accessibility (98), best practice (100) and SEO (100) as in the desktop test. The relatively low score in performance was partly because of "Largest Contentful Paint element". This was regarding the hero image. The image is small (around 60 kB) and has webp format which eliminates the image itself to be the problem. The part which took the largest time was load delay. This can be caused by Cloudinary, where the images are stored. The time it takes for the Cloudinary server to serve the images, can increase the load delay for the webpage. There are several ways to solve the problem. Since the main problem seems to be Cloudinary, a way to improve is to use another service. It can be GitHub, Amazon S3 or any similar service. If the use of Cloudinary should continue, it could be a good idea to get a paid account to get faster server service.

### Wave Webaim - accessibility testing

The accessibility test at [Wave Webaim](https://wave.webaim.org/) resulted without errors and contrast errors on all pages.

#### Index page

![Wave webaim test of index page](doc/wave-webaim.webp)

#### About page

![Wave webaim test of about page](doc/wave-webaim-about.webp)

#### Booking page

![Wave webaim test of about page](doc/wave-webaim-booking.webp)

### Contrast Grid

The [Contrast Grid](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23CACACA%2C%20%20Background%20color%0D%0A%23353535%2C%20Text%0D%0A%23411919%2C%20Cancel%20btn%20-%20background%0D%0A%23FFFFFF%2C%20Cancel%2Fconfirm%2Fdelete%20btn%20-%20text%0D%0A%23193A18%2C%20Confirm%20btn%20-%20background%0D%0A%238d3838%2C%20Delete%20btn%20-%20background%0D%0A%23000000%2C%20Footer%20icons&es-color-form__tile-size=compact&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp) resulted in only AAA results for the combination used on the webpage. The main combination throughout the page is #CACACA and #353535 which has a value of 7.4 (where the limit for AAA is 7+).

![Contrast Grid of the webpage](doc/contrast-grid.webp)

### Automated Testing

Automated testing is done for all three different apps (about, booking and news). In total, 33 tests were made - 8 tests in about, 12 tests in booking and 13 tests in news.

![Automated tests for all apps](doc/tests-all.webp)

#### About

![Automated tests for about app](doc/tests-about.webp)

- [Test of forms.py](about/tests_forms.py)
- [Test of views.py](about/tests_views.py)

#### Booking

![Automated tests for booking app](doc/tests-booking.webp)

- [Test of models.py](booking/tests_models.py)
- [Test of views.py](booking/tests_views.py)

#### News

![Automated tests for news app](doc/tests-news.webp)

- [Tests of admin.py](news/tests_admin.py)
- [Tests of models.py](news/tests_models.py)
- [Tests of views.py](news/tests_views.py)

### Manual Testing

Every page at the website has been manually tested. It is done in Google Chrome DevTools and on different devices. The devices used were one mobile phone, one laptop and one external screen:

- Samsung Galaxy A52s (1080 x 2400)
- HP 250 G4 Notebook PC (1366 x 768)
- HP 2309v LCD Screen (1920 x 1080)

#### Navigation bar

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Home link | When clicked, directs the user to the home page | Click at "Home" | Got directed to the home page | Pass |
| About link | When clicked, directs the user to the about page | Click at "About" | Got directed to the about page | Pass |
| Booking link | When clicked, directs the user to the booking page | Click at "Booking" | Got directed to the booking page | Pass |
| Sign up link | When clicked, directs the user to the sign up page | Click at "Sign up" | Got directed to the sign up page | Pass |
| Sign in link | When clicked, directs the user to the sign in page | Click at "Sign in" | Got directed to the sign in page | Pass |
| News link not visible (signed out) | News link not visible as a signed out user | Sign out and inspect navigation bar | News link not visible | Pass |
| News link not visible (signed in user - regular) | News link not visible as a signed in user (without staff or superuser credentials) | Sign in as a regular user, check navigation bar | News link not visible | Pass |
| News link visible (signed in user - staff or superuser) | News link visible as a signed in user (with staff or superuser credentials) | Sign in as staff or superuser, check navigation bar | News link visible | Pass |
| News link | When clicked, directs the signed in user (staff or superuser) to the news page | Sign in as a staff or superuser, click at "News" | Got directed to the news page | Pass |
| My bookings link not visible | My bookings link not visible as a signed out user | Sign out and inspect navigation bar | My bookings link not visible | Pass |
| Me bookings link visible | My bookings link visible as a signed in user | Sign in, check navigation bar | My bookings link visible | Pass |
| Username showing (signed in user) | When the user is signed in, the username is presented as the link to my bookings | Sign in, check navigation bar | Username is showing | Pass |
| My bookings link | When clicked, directs the signed in user to my bookings page | Click at username | Got directed to the my bookings page | Pass |
| Sign out link | When clicked, directs the user to the sign out page | Click at "Sign out" | Got directed to the sign out page | Pass |

#### Index page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The index page was responsive and changed depending on screen size | Pass |
| "Check out available workshops" button | Directs the user to the Booking page | Click at the "Check out available workshops" button | Got directed to the Booking page | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| Sign up button visible (not signed in) | The sign up button below member benefits is visible when the user isn't signed in | Sign out and check below member benefits | Sign up button is visible | Pass |
| Sign up button not visible (signed in) | The sign up button below member benefits is not visible when the user is signed in | Sign in and check below member benefits | Sign up button isn't visible | Pass |
| Text at image carousel | The text at the image carousel is readable | Read the text at all Bootstrap breakpoints | The text is readable | Pass |
| Start image in carousel | Start image is always the one with "Fancy some inspiration" text | Browse through the image carousel and leave it at different images before refreshing the page | The carousel always begins at "Fancy some inspiration" image | Pass |
| Image carousel never stops | The carousel doesn't stop, when all images are showed it starts over again | Browse through all images at both directions | When the last image is shown, the first image appears when the next arrow is pressed | Pass | 

#### About page
		
| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The about page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| Contact form validation | A message appears if the user doesn't fill out all fields | Fill out all fields except one, let all different fields (First name, Last name, Email and Message) be the empty field one by one | A message appears when a field is left empty | Pass |
| Contact form response | Response appears, confirming to the user that the form has been sent | Fill out the form with valid input and press Submit | The contact form changed into a message confirming that the message has been sent | Pass |
| Contact form message recieved | The submitted form is sent to selected inbox in Mailtrap | Fill out the form with valid input and press Submit, log in to Mailtrap and view selected inbox | The message from the contact form are sent to Mailtrap | Pass |

#### Booking page
		
| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The booking page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| Read more button - Perler beads | The text about Perler beads workshop expands and shows more text when the "Read more" button is pressed | Press "Read more" in the Perler beads card | The text expanded and showed more text | Pass |
| Read less button - Perler beads | The expanded text about Perler beads workshop goes back to "normal" when the "Read less" button is pressed | Press "Read less" in the Perler beads card | The text collapsed and went back to normal | Pass |
| Read more button - Transforming treasures | The text about Transforming treasures workshop expands and shows more text when the "Read more" button is pressed | Press "Read more" in the Transforming treasures card | The text expanded and showed more text | Pass |
| Read less button - Transforming treasures | The expanded text about Transforming treasures workshop goes back to "normal" when the "Read less" button is pressed | Press "Read less" in the Transforming treasures card | The text collapsed and went back to normal | Pass |
| Read more button - Our ultimate crafting experience | The text about Our ultimate crafting experience workshop expands and shows more text when the "Read more" button is pressed | Press "Read more" in the Our ultimate crafting experience card | The text expanded and showed more text | Pass |
| Read less button - Our ultimate crafting experience | The expanded text about Our ultimate crafting experience workshop goes back to "normal" when the "Read less" button is pressed | Press "Read less" in the Our ultimate crafting experience card | The text collapsed and went back to normal | Pass |
| Booking buttons - trigger modal | When a booking button is pressed, a confirmation modal is triggered | Click all booking buttons | All booking buttons triggered a confirmation modal | Pass |
| Confirmation modal - X | When the X at the confirmation modal is pressed, the modal is closed without making any booking | Trigger confirmation modal, press X | The modal closed without making any booking | Pass |
| Confirmation modal - Close | When the "Close" button at the confirmation modal is pressed, the modal is closed without making any booking | Trigger confirmation modal, press "Close" | The modal closed without making any booking | Pass |
| Confirmation modal - outside modal | When the user clicks anywhere outside of the confirmation modal, it is closed without making any booking | Trigger confirmation modal, click somewhere outside of the modal | The modal closed without making any booking | Pass |
| Confirmation modal - Confirm | When the "Confirm" button is pressed, a booking is made | Press "Confirm", check "My bookings" if a booking has been made | A booking was made | Pass |
| Confirmation modal - Confirm | When the "Confirm" button is pressed, the user gets redirected to Success page | Press "Confirm" | The user got directed to the Success page | Pass |
| Pagination | When it is more than eight upcoming workshops, pagination appears | Scroll down below active bookings buttons | After eight bookings, pagination buttons appears | Pass |
| Pagination - stay at bookings buttons section | When you change between the pages of active booking buttons, you come to the top of the booking buttons | Change page using pagination | When next button is pressed, the second page is showed and scrolled to the top of booking buttons | Pass |
| Double booking modal | When a user tries to book a workshop session they already has a booking at, a Booking notice modal is triggered | Try to book a workshop where an active booking already exists | A modal is triggered when the user tries to double book | Pass |
| Double booking modal - X | When the X at the double booking modal is pressed, the modal is closed without making any booking | Trigger double booking modal, press X | The modal closed without making any booking | Pass |
| Double booking modal - Close | When the "Close" button at the double booking modal is pressed, the modal is closed without making any booking | Trigger double booking modal, press "Close" | The modal closed without making any booking | Pass |

#### Success page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| View my bookings button | The "View my bookings" button directs the user to My bookings page | Click at "View my bookings" button | The user got directed to the My bookings page | Pass |
| Book another workshop button | The "Book another workshop" button directs the user to Bookings page - booking buttons section | Click at "Book another workshop" | The user got directed to the Booking page, booking buttons section | Pass |
| Home button - not visible | On devices smaller than 768px (breakpoint below medium in Bootstrap), the "Home" button is not visible | Select breakpoint smaller than medium and view the page | The "Home" button is not visible | Pass |
| Home button - visible | On devices with 768px or larger (breakpoint medium or larger in Bootstrap), the "Home" button is visible | Select medium breakpoint and view the page | The "Home" button is visible | Pass |

#### My bookings page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| Username in text | In the first sentence, the username is presented | Sign in and compare the username with the presented name | The username and the presented name is equal | Pass |
| Active bookings | All of the user's active bookings are presented | Compare active bookings in the admin panel to the presented active bookings | The active bookings are the same in the admin panel as presented at My bookings page | Pass |
| Edit button | When the "Edit" button is pressed, the user gets directed to Edit booking page | Press "Edit" button | The user got directed to Edit booking page | Pass |
| Cancel button | When the "Cancel" button is pressed, a confirmation modal is triggered | Press "Cancel" button | A confirmation modal is triggered | Pass |
| Confirmation modal - X | When the X at the confirmation modal is pressed, the modal is closed without cancelling the booking | Trigger confirmation modal, press X | The modal closed without cancelling the booking | Pass |
| Confirmation modal - Close | When the "Close" button at the confirmation modal is pressed, the modal is closed without cancelling the booking | Trigger confirmation modal, press "Close" | The modal closed without cancelling the booking | Pass |
| Confirmation modal - outside modal | When the user click anywhere outside of the confirmation modal, it is closed without cancelling the booking | Trigger confirmation modal, click somewhere outside of the modal | The modal closed without cancelling the booking | Pass |
| Confirmation modal - Confirm | When the "Confirm" button is pressed, the booking is cancelled | Trigger confirmat modal, press "Confirm", check "My bookings" if the booking has been cancelled | The booking was cancelled | Pass |
| Available spots increase | When a booking is cancelled, available spots are increased by one | Check available spots at an already booked workshop, cancel the booking and check available spots again | Available spots increased by one | Pass |
| Pagination | When it is more than four upcoming workshops, pagination appears | Scroll down below my bookings buttons | After four bookings, pagination buttons appears | Pass |
| No bookings - text | A text about no bookings were found appears at the top of the page | Cancel all the user's bookings | No bookings were found text appeared | Pass |
| No bookings - Take me there button | The "Take me there" button directs the user to booking page | Click at "Take me there" button | The user got directed to booking page | Pass |

#### Edit booking page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| Available workshop sessions | Only sessions where the user doesn't already have an active booking is shown | Compare upcoming workshops, the user's active bookings and the available sessions in edit booking | Only sessions where the user doesn't have an active booking are visible | Pass |
| Booking buttons - trigger modal | When a booking button is pressed, a confirmation modal is triggered | Click all booking buttons | All booking buttons triggered a confirmation modal | Pass |
| Confirmation modal - X | When the X at the confirmation modal is pressed, the modal is closed without making any booking | Trigger confirmation modal, press X | The modal closed without making any booking | Pass |
| Confirmation modal - Close | When the "Close" button at the confirmation modal is pressed, the modal is closed without making any booking | Trigger confirmation modal, press "Close" | The modal closed without making any booking | Pass |
| Confirmation modal - outside modal | When the user click anywhere outside of the confirmation modal, it is closed without making any booking | Trigger confirmation modal, click somewhere outside of the modal | The modal closed without making any booking | Pass |
| Confirmation modal - Confirm | When the "Confirm" button is pressed, the existing booking is changed to the selected workshop session | Trigger confirmation modal, press "Confirm", check "My bookings" if the booking has been changed | The booking was changed | Pass |
| Available spots - increase | In the session the user cancel their booking, available spots increases by one | Check available spots at the session, edit the booking, check available spots again | Available spots increased by one | Pass |
| Available spots - decrease | The available spots in the new session the user chooses, decreases by one | Check available spots at the session, edit the booking, check available spots again | Available spots decreased by one | Pass |
| Pagination | When it is more than eight available workshops, pagination appears | Scroll down below active bookings buttons | After eight bookings, pagination buttons appears | Pass |

#### News page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| Color change - every other | Every other news have dark backgrounds, every other light backgrounds | Scroll through the news | Every other news has dark background, every other news has light background | Pass |

#### Sign up page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| All fields required | An error message appears when the user tries to sign up but leaves one field empty | Leave one field empty one by one and try to Sign Up | An error message appeared when a field was left empty | Pass |
| Redirected | When the "Sign Up" button is pressed, the user gets redirected to the page they visited before | Visit Booking page, click Sign up, fill out all required fields, press "Sign Up" button | The user got redirected to Booking page | Pass |

#### Sign in page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| All fields required | An error message appears when the user tries to sign in but leaves one field empty | Leave one field empty one by one and try to Sign In | An error message appeared when a field was left empty | Pass |
| Sign In button | When the "Sign In" button is pressed, the user gets signed in | Click at "Sign In" button | The user gets signed in | Pass |
| Redirected | When the "Sign In" button is pressed, the user gets redirected to the page they visited before | Visit Booking page, click Sign in, press "Sign In" button | The user got redirected to Booking page | Pass |

#### Sign out page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| Sign Out button | When the "Sign Out" button is pressed, the user gets signed out | Click at "Sign Out" button | The user gets signed out | Pass |
| Redirected | When the "Sign Out" button is pressed, the user gets redirected to the page they visited before | Visit Booking page, click Sign out, press "Sign Out" button | The user got redirected to Booking page | Pass |

#### 404 page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| Return to stability button | When "Return to stability" button is pressed, the user gets directed to the home page | Click at "Return to stability" button | The user got directed to the home page | Pass |

#### 500 page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| Link to homepage | When the link to the homepage is clicked, the user gets directed to the homepage | Click at homepage link | The user got directed to the homepage | Pass |
| Link to contact form | When the link to the contact form is clicked, the user gets directed to the contact form | Click at the link to the contact form | The user got directed to the contact form | Pass | 

#### Footer

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The footer changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The footer was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| Link to contact form | When the pencil icon is clicked, the user gets directed to the contact form | Click at the pencil icon | The user got directed to the contact form | Pass |
| Link to Facebook | When the Facebook icon is clicked, the user gets directed to Facebook which opens in a new tab | Click at the Facebook icon | The user got directed to Facebook which opens in a new tab | Pass |
| Link to Instagram | When the Instagram icon is clicked, the user gets directed to Instagram which opens in a new tab | Click at the Instagram icon | The user got directed to Instagram which opens in a new tab | Pass |
| Link to Pinterest | When the Pinterest icon is clicked, the user gets directed to Pinterest which opens in a new tab | Click at the Pinterest icon | The user got directed to Pinterest which opens in a new tab | Pass |

### Bugs

During the testing several bugs have been discovered. No bugs were left unfixed.

When the html validation of all pages were completed, it summed up 95 errors. This high amount of errors were caused by repeated errors. The most common error was that the button element had prohibited child element. Both divs and h6 elements were child to buttons. This was corrected before the final version was deployed.

Another validation error that occured at several places were that "hx not allowed on element form". This was solved by adding "data-" in front of the hx. 

A third validation error that was recurring through the different pages was that form action was left empty. This was solved by deleting form action since it wasn't used.

When the PEP8 validation of the Python code was made, 39 errors occured. Most of them were one of following:
- trailing whitespace
- line too long
- blank line contains whitespace

After the first Lighthouse test, the SEO was 90. To enhance this, meta tags with description and keywords were added. This increased the score to 100. 

## Technologies Used

The repository is created from [Code Institutes Gitpod full template](https://github.com/Code-Institute-Org/gitpod-full-template) through [GitHub](https://github.com/). The Project board is created at [GitHub](https://github.com/). The code is written in [Gitpod](https://www.gitpod.io/) and deployed at [Heroku](https://www.heroku.com/). The wireframes are created in [Balsamiq](https://balsamiq.com/) and the ERD's are created in [Google Spreadsheet](https://docs.google.com/spreadsheets/).

The code languages used in this project are HTML, CSS, JavaScript and Python. The main frameworks used are Django and Bootstrap.

## Deployment

### Fork repository in GitHub

- Open the chosen repository in GitHub 
- Click on the "Fork" button
- A copy of the repository is now located in your own account

### Clone repository in GitHub

- Open the chosen repository in GitHub 
- Click on "Code" button
- Copy the URL
- Open your command line interface
- Navigate to the directory you want to clone the repository to
- Use 'git clone', followed by the earlier copied URL
- Move into the newly created directory
- Install the dependencies using 'pip install -r requirements.txt'
- Run the application with 'python manage.py runserver'

### Deployment to Heroku

- Open Heroku and log in
- Click on "New" and choose the option "Create new app"
- Choose an app name and which region (Europe or United States) you are located in
- Press "Create app"
- When the app is created, choose the Settings tab
- Under "Config Vars", press "Reveal Config Vars"
- In keys, write DATABASE_URL
- In value, insert the url to the database
- Press "Add"
- Under "Buildpacks", press "Add buildpack"
- Choose "Python", press "Add buildpack"
- Change tab to the Deploy tab
- Choose deploy method - GitHub
- Search for the correct repository name at your connected GitHub account
- Press "Connect"
- Under "Manual deploy", choose which branch to deploy and press "Deploy Branch"

Link to deployed website: <https://frisa-booking-e7f1e4a00ea9.herokuapp.com/>

## Credits

### Libraries used

| Library | Functionality |
| ------------------- | --------------------------------- |
| django-allauth | Used for authentication, registration and account management |
| django-summernote | Integrated editor in djangos admin panel |
| gunicorn | Used to run Python web applications |
| htmx | Used for response in contact form |
| oauthlib | Used to implement OAuth functionality |
| sendgrid | For interacting with the SendGrid email service |
| urllib3 | Used to make HTTP requests |
| whitenoise | Simplifies static file serving for Python web apps |

### Used resources

| Page | Used for |
| --------------| ----------------- |
| [Djecrety](https://djecrety.ir/) | Generate a secret key |
| [Font Awesome](https://fontawesome.com/) | All icons at the website |
| [Code with Stein](https://github.com/SteinOveHelset/contactform) | Creating contact form |
| [Flavio Copes](https://flaviocopes.com/how-to-add-event-listener-multiple-elements-javascript/) | How to add event listener to multiple elements |
| [W3Schools](https://www.w3schools.com/howto/howto_js_read_more.asp) | Base for read more/read less buttons |
| [Medium](https://medium.com/@biswajitpanda973/django-model-relationships-11ef9d73168d ) | Knowledge about double underscore |
| [htmx](https://htmx.org/docs/ ) | Knowledge about htmx |
| [django](https://docs.djangoproject.com/) | Knowledge about django |
| [Emojipedia](https://emojipedia.org/) | Select emojis |

### Images

| Page | Used for |
| ------------- | --------------- |
| [Vecteezy](https://www.vecteezy.com/vector-art/8322134-elegant-floral-line-art-seamless-pattern) | Background image at member benefits section, from [Agnet Art](https://www.vecteezy.com/members/agnetart) |
| [Vecteezy](https://www.vecteezy.com/photo/36594863-ai-generated-craft-shop-advertisment-background-with-copy-space) | Background image at 404 page, from [Oleg Gapeenko](https://www.vecteezy.com/members/gankogroup) |
| [Vecteezy](https://www.vecteezy.com/photo/2264081-galactic-center-of-the-milky-way-with-many-colors-on-a-starry-sky-in-deep-space) | Background image at 500 page, from [TheCatEmpire Studio](https://www.vecteezy.com/members/thecatempirestudio) |
| [BeFunky](https://www.befunky.com/) | Edit and resize images |
| [Pixelied](https://pixelied.com/convert) | Convert images to webp |
| [TinyPNG](https://tinypng.com/) | Compress images |

The profile photo at the about page is taken by Linus Wikell. All other photos are taken by the website creator, [Frida Wikell](https://github.com/FridaWikell).

## Acknowledgements

A big thanks to Matt Bodden for invaluable thoughts and ideas in how to get the project going in the right direction!

Hats off to my proofreading master, Linus Wikell!

[Back to top](#frisa-booking)