# Reddit-Style News Site

The Reddit-Style News Site is a Django-based full-stack web application where users can create posts, comment, and upvote posts and comments. The platform features a categorized system to organize content and interactions through voting.

**I need to add Images here**

## Features

### Existing Features

- **User Registration and Authentication**
  - Users can register for an account, log in, and log out using Django's built-in authentication.
  - Authentication checks ensure that only registered users can interact with certain features such as creating posts, commenting, and upvoting.

- **Post Creation and Categories**
  - Authenticated users can create posts. Each post has a title, content, and an optional category.
  - Categories help organize posts.

- **Commenting System**
  - Users can comment on posts. Comments are displayed under the post and are available for viewing by all users.
  - Only authenticated users can add comments, and they are saved under the user who posted them.

- **Upvoting System**
  - Both posts and comments can be upvoted by authenticated users.
  - Users can only upvote a post or comment once, ensuring fair voting.
  - The upvote count is displayed next to each post and comment and is updated in real-time.

- **CRUD Functionality**
  - **Create**: Authenticated users can create new posts and comments.
  - **Read**: All users can read posts, comments, and browse by category.
  - **Update**: Users can edit their own posts directly from the front end.
  - **Delete**: Users can delete their own posts without needing to access the admin panel.

- **Dynamic User Interface**
  - The website features a responsive UI using Bootstrap for styling.
  - UI includes buttons for creating, editing, deleting, and upvoting posts/comments.

### Features Left to Implement

- **User Profiles**
  - Allow users to customise their own profile. Add information like, location, age ,etc

- **Social Features**  
  - Adding a "follow" feature for users to follow each other and view posts from followed users.

- **Sorting and Filtering**
  - Adding sorting options such as "Most Upvoted" or "Newest" for posts to provide a more customized experience.

- **Social Sharing**
  - Adding options for users to share posts directly to social media.

## Planning and Development

### Site Planning Steps:
- **Initial Setup**:
  - Set up Django project and configure environment.
  - Set up a GitHub repository and managed version control using Git.
- **User Stories and GitHub Project Board**:
  - Used Agile methodologies for planning. User stories were tracked using GitHub Project Boards.
- **Model Creation**:
  - Created models for `Post`, `Comment`, `Category`, and `UserProfile`.
- **Backend Features**:
  - Implemented CRUD functionalities, category assignment, and the upvoting system.
- **Frontend Implementation**:
  - Created responsive templates using HTML, CSS (Bootstrap), and implemented forms for post creation and comment interaction.
- **Deployment**:
  - Set up environment variables, used Whitenoise for static file handling, and deployed on Heroku.  