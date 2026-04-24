# UOW Room Booking System

This project is a front-end web application built for the University of Wollongong (UOW) as part of a web development assignment. It simulates a staff-facing room booking and management system, allowing staff to create, view, edit, and manage room bookings through a multi-page interface.

The system is built entirely with HTML, CSS, and vanilla JavaScript, with no backend or database — all data is persisted using the browser's `sessionStorage` and `localStorage` APIs. The focus is on interface design, component consistency, user flow, and practical implementation of front-end web development concepts.

## What This Project Shows

- Multi-page web application structure with consistent navigation
- CRUD operations (Create, Read, Update, Delete) implemented in vanilla JavaScript
- Data persistence using browser storage APIs
- Responsive, component-driven UI design with a shared CSS system
- Dynamic DOM manipulation and real-time filtering
- Form validation and conditional UI logic
- Dark mode theming applied globally across all pages

## Tech Stack

- HTML5
- CSS3 (custom properties, flexbox, grid)
- Vanilla JavaScript (ES6+)
- Browser Storage (`localStorage`, `sessionStorage`)
- No frameworks, no libraries, no build tools

## Pages

### `login.html` — Login
Entry point of the application. Authenticates the user before granting access to the dashboard.

### `staff-dashboard.html` — Staff Dashboard
Main hub after login. Provides navigation to all major features: Create Room, History, Manage, and Schedule.

### `create.html` — Create Room
A form-based page that allows staff to create a new room booking. Fields include room type, capacity, charging port availability, date, time range, block and room number, price, equipment checkboxes, and a photo upload.

### `history.html` — Booking History
Displays all previously created room bookings loaded from `localStorage`. Each card shows room type, date, time, and price. Future bookings show both an **EDIT** and a **DETAIL** button; past bookings show only **DETAIL**.

### `edit.html` — Edit Room
Pre-fills all fields from a selected room booking and allows the user to update any detail. Accessed by passing the room ID as a URL query parameter (`?id=...`). Saves the updated data back to `localStorage`.

### `detail.html` — Room Detail
A read-only view of a room booking. All fields are displayed as static text with no editable inputs. Accessed from both History and Manage pages.

### `manage.html` — Manage Rooms
A staff management view showing all rooms with a filter sidebar. Rooms can be filtered by capacity and room type using checkboxes. Each room card links to the Detail page.

### `schedule.html` — Schedule
Displays a navigable monthly calendar. Dates with existing bookings are marked with a dot indicator. Clicking a date shows all rooms booked on that date in a card list, each linking to the Detail page.

### `settings.html` — Settings
A settings page with Theme, Language, and Accessibility options styled as pill-shaped rows. The Theme row expands to reveal a Dark Mode toggle that applies a global dark theme across all pages using `sessionStorage`.

## Key Features

- **Shared header and navigation panel** across all pages — UOW logo, bell, user, and logout icons in the header; a slide-in hamburger side panel with links to all sections
- **Clickable logo** on all logged-in pages that returns the user to the staff dashboard
- **Real-time filter** on the Manage page using capacity and room type checkboxes
- **Calendar with booking indicators** on the Schedule page, with month navigation and date-based filtering
- **Conditional EDIT button** on History — only shown for future or current-day bookings, not past ones
- **Global dark mode** — toggled from Settings, persisted via `sessionStorage`, and applied instantly on page load via an inline `<head>` script to prevent flash

## Project Structure

```
/
├── login.html
├── staff-dashboard.html
├── create.html
├── edit.html
├── detail.html
├── history.html
├── manage.html
├── schedule.html
├── settings.html
├── loggedin.css          ← Shared stylesheet for all logged-in pages
├── base.js               ← Shared JS for side panel and dark mode init
└── assets/
    └── uowlogo.svg
```

## Notes

- This project was completed as an academic assignment and is included here as a code and design sample.
- All data is stored client-side, there is no server, database, or authentication backend.
- Dark mode persistence relies on `sessionStorage` rather than `localStorage` due to sandboxed iframe restrictions in some hosting environments.
- The "Booked by" field on the Schedule page is a placeholder, user account linking is not implemented in this version.
- Some buttons and functions are not functional, which was intentional, as the main purpose was to showcase the booking and history as per Hi-Fi prototypes done up per the assignment.

## Improvement Areas

If revisited, the following improvements would be considered:

- Adding a real authentication system with user roles (admin vs. student)
- Replacing `sessionStorage` with a backend database for true data persistence across sessions
- Adding a date picker validation to prevent booking past dates
- Implementing a booking conflict check to prevent double-booking the same room and time slot
- Making the Language and Accessibility settings functional
- Adding mobile responsiveness across all pages
- Introducing JavaScript modules to reduce code duplication across pages
