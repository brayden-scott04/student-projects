# Web Development Projects

This folder contains selected frontend development assignments from my web development coursework. The projects are uploaded as code-first portfolio samples to demonstrate my understanding of HTML, CSS, JavaScript, DOM manipulation, form handling, input validation, interactive browser-based UI logic, and structured data transformation.

These assignments were originally completed for school, but I’ve organized them here so the code is easier to review. The focus is on implementation quality, problem-solving approach, and practical web development skills.

## What this folder shows

- Semantic HTML structure and page layout
- CSS styling for formatting, spacing, tables, and visual presentation
- JavaScript for validation, event handling, DOM updates, and game logic
- User interaction design through forms, buttons, and dynamic content
- Structured data modeling with XML
- Data validation using XSD
- Data transformation and presentation using XSLT

## Tech Stack

- HTML5
- CSS3
- JavaScript (Vanilla JS)
- DOM API
- XML
- XSD (XML Schema)
- XSLT

## Projects

### A1 — Frontend Fundamentals: Structured Content, Validation, and Utility Form

A multi-section browser-based assignment combining structured content presentation, static page layout, formatted code display, institutional information sections, and a functional interactive form. This project demonstrates early frontend fundamentals with increasing complexity across content structure, styling, and client-side scripting.

#### Scope
- Student information table layout
- Internal page navigation with anchor links
- “Hello World” examples in multiple languages
- Styled content sections for university services and policies
- Interactive form with validation and utility features

#### Key Features
- Real-time name validation using regular expressions
- Module code validation with custom format rules
- Auto-generated current date and time field
- Find-and-replace logic inside a textarea
- Language selection UI with external translation launch
- Reset workflow to restore default form state
- Mixed use of tables, floated images, preformatted code blocks, and structured content

#### Technical Concepts Demonstrated
- DOM selection with `getElementById` and `querySelector`
- Event listeners for `input` and `click`
- Regex validation for form fields
- Conditional UI states such as enabling and disabling inputs
- String processing with `split()` and `join()`
- Dynamic text updates with `innerHTML` and `value`
- Date formatting with JavaScript `Date`

### A2 — Interactive Browser Game and XML Weather Forecast Transformation

This assignment has two parts: one focused on JavaScript interactivity, and the other focused on XML, XSD, and XSLT for validation and presentation.

#### Part 1 — Interactive Character Matching Game

A browser game built with HTML and Vanilla JavaScript where the player enters a name, selects a target character, starts the round, and gains or loses points by clicking the correct character as the board updates over time.

##### Key Features
- Player name input used to unlock gameplay controls
- Character selection before the round begins
- Randomized three-cell board updated at timed intervals
- Score increases for correct clicks and decreases for incorrect ones
- Highest-score tracking within the session
- Start and stop controls with game-state locking

##### Technical Concepts
- DOM manipulation
- Event handling
- Conditional UI state management
- Arrays and random selection
- `setInterval()` and `clearInterval()`
- Interactive score updates


#### Part 2 — XML Weather Forecast with XSD Validation and XSLT Rendering

A structured data project that stores weather forecast entries in XML, validates the data using XSD, and transforms it into an HTML weather table using XSLT. It shows how weather data can be structured, validated, and displayed in a readable format.

##### Key Features
- XML forecast dataset with weather entries and metadata
- XSD schema defining valid structure, attributes, and value constraints
- XSLT transformation that converts XML into an HTML table
- Sorted weather records using date-based ordering
- Conditional rendering of weather icons and text colors
- Day-based table cell generation using reusable XSL templates

##### Technical Concepts Demonstrated
- XML document structure and attributes
- XSD simple and complex types
- Schema restrictions such as ranges and enumerations
- XSLT templates, parameters, variables, and conditional logic
- Data transformation from XML to browser-rendered HTML
- Reusable template design for table cell generation

## Skills Demonstrated

| Skill Area | Evidence Across Projects |
|---|---|
| HTML Structure | Tables, forms, sections, navigation links, content blocks |
| CSS Styling | Layout formatting, spacing, colors, floats, table styling |
| JavaScript Fundamentals | Variables, functions, arrays, loops, conditionals, string operations |
| DOM Manipulation | Dynamic text updates, validation feedback, score display changes, control states |
| Form Validation | Regex checks, empty-field detection, error messaging |
| UI Interactivity | Buttons, click events, form actions, reset flows, live updates |
| State Management | Game running state, input locking, score tracking, form control toggling |
| Data Modeling | XML forecast structure with attributes and nested records |
| Data Validation | XSD restrictions, required attributes, enumerated values |
| Data Transformation | XSLT templates, sorting, conditional rendering, HTML output generation |

## Notes

- These projects were originally completed as academic assignments and are included here as code samples.
- Only core source code files are included in this folder.
- Some original assets or submission-related supporting files may not be included.
- The focus of this repository is code review, technical clarity, and implementation quality.

## Improvement Areas

If these projects were revisited for production polish, I would improve them further by:

- Separating HTML, CSS, and JavaScript into dedicated files where appropriate
- Replacing inline styles with reusable class-based styling
- Improving naming consistency and modularity
- Adding accessibility improvements such as clearer labels and semantic enhancements
- Strengthening responsive design for different screen sizes
- Refactoring repeated logic into reusable helper functions


