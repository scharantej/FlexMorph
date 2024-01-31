## Flask Application Design for Dynamic Landing Page of a 4 Wheeler SUV Car

### HTML Files

- **index.html:**
  - Main landing page of the application.
  - Contains the HTML structure for the dynamic landing page.
  - Includes necessary CSS and JavaScript files for animations and interactivity.

- **car-assembly.html:**
  - HTML file for the car assembly section of the landing page.
  - Displays the 4 wheeler SUV car in a disassembled state.
  - Provides buttons or triggers to initiate the car assembly animation.

- **car-dismantle.html:**
  - HTML file for the car dismantle section of the landing page.
  - Displays the fully assembled 4 wheeler SUV car.
  - Provides buttons or triggers to initiate the car dismantle animation.


### Routes

- **index:**
  - Route for the main landing page.
  - Serves the `index.html` file when a user accesses the application's root URL.

- **assemble:**
  - Route for the car assembly section.
  - Serves the `car-assembly.html` file when triggered by a user action (e.g., clicking a button).

- **dismantle:**
  - Route for the car dismantle section.
  - Serves the `car-dismantle.html` file when triggered by a user action (e.g., clicking a button).

- **static:**
  - Route to serve static files such as CSS and JavaScript used in the HTML files.
  - This ensures that the necessary resources are accessible by the browser.


### Explanation

The HTML files define the structure and content of the dynamic landing page, including the car assembly and dismantle sections. The routes specify how the application responds to user actions and serves the appropriate HTML files.

When a user accesses the root URL of the application, the `index` route serves the `index.html` file, displaying the main landing page. Triggering a user action (e.g., clicking a button) initiates the car assembly or dismantle animation, causing the application to serve either the `car-assembly.html` or `car-dismantle.html` file, respectively.

The `static` route ensures that the CSS and JavaScript files necessary for the animations and interactivity are accessible to the browser.

This design allows for a seamless and dynamic landing page experience, showcasing the process of assembling and dismantling a 4 wheeler SUV car as the user interacts with the page.