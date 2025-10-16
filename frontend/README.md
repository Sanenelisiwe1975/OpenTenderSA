# OpenTender SA Frontend

This is the React + TailwindCSS dashboard for OpenTender SA.

## Features
- Browse tenders by department/province
- View flagged irregularities
- See statistics (vendor dominance, average delays)
- Submit anonymous reports securely

## Setup

1. Install dependencies:
   ```bash
   npm install
   ```

2. Start the development server:
   ```bash
   npm run dev
   ```

3. Access the dashboard at [http://localhost:3000](http://localhost:3000)

## Structure
- `src/pages/Dashboard.js`: Main dashboard view
- `src/pages/Report.js`: Anonymous reporting form
- `src/components/NavBar.js`: Navigation bar
- `src/App.js`: Routing and layout

## Styling
TailwindCSS is used for rapid UI development. You can customize styles in `tailwind.config.js`.