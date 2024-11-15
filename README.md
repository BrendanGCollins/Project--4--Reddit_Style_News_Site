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

## Libraries Used

- **Django**: Main framework used for web development and back-end.
- **Bootstrap**: Used to create a responsive design.
- **Gunicorn**: WSGI server used for running the app on Heroku.
- **Whitenoise**: Static file management to serve CSS, JavaScript, and image files during deployment.

## Testing

- **Manual Testing**: Each feature has been manually tested to ensure proper functioning.
- **Automated Testing**: 
  
  _

### Manual Testing

| Action | Expected Behaviour | Pass or Fail | Notes |
|--------|--------------------|--------------|-------|
| User Registration | User should be able to register an account and receive a confirmation message | Pass | |
| Login and Logout | User should be able to log in and log out of their account | Pass | |
| Create a Post | Logged-in users can create new posts with title and content | Pass | |
| Create a Comment | Logged-in users can comment on posts, and the comment is displayed below the post | Pass | |
| Upvote a Post | User can upvote a post, and the count updates | Pass | |
| Upvote a Comment | User can upvote a comment, and the count updates | Pass | |
| Edit Post | Users can edit only their own posts | Pass | |
| Delete Post | Users can delete their own posts | Pass | |
| Prevent Unauthorized Access | Unauthorized users cannot access restricted actions like creating a post or commenting | Pass | |

### Unfixed Bugs

No known bugs were found at the time of project completion.

## Deployment

### GitHub

The project was deployed to GitHub for version control and collaboration. The link to the GitHub repository is:

- [GitHub Repository Link](https://github.com/BrendanGCollins/Project--4--Reddit_Style_News_Site)

### Heroku

The site was also deployed on **Heroku**. Below are the steps taken for deployment:

1. **Step 1**: Sign up or log in to **Heroku**.
2. **Step 2**: Ensure you have a `requirements.txt` file that contains all dependencies.
3. **Step 3**: Create a new Heroku application.
4. **Step 4**: Connect to GitHub and choose the repository containing the project.
5. **Step 5**: Set environment variables including `SECRET_KEY` and configure `DEBUG = False`.
6. **Step 6**: Add `whitenoise` and `gunicorn` to handle static files and manage the WSGI server.
7. **Step 7**: Deploy the project and test to ensure the app is working correctly.

The live link to the project can be found here:

- [Live Heroku Deployment](https://reddit-style-news-site-44d5820c6a01.herokuapp.com/)

## Credits

- **Stack Overflow**: Helpful discussions and solutions for debugging.
- **YouTube Tutorials** - Channels such as `Traversy Media` and `Academind` helped to understand Django features.

### Libraries

- **Django**: Used for creating models, views, and handling back-end functionalities.
- **Bootstrap**: For a responsive and user-friendly front-end.
- **Whitenoise**: Static file handling for deployment on Heroku.
- **Gunicorn**: Used for deployment as the WSGI server.  