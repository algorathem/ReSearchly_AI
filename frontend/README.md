# Welcome to your Lovable project

## Project info

**URL**: https://lovable.dev/projects/REPLACE_WITH_PROJECT_ID

## How can I edit this code?

There are several ways of editing your application.

**Use Lovable**

Simply visit the [Lovable Project](https://lovable.dev/projects/REPLACE_WITH_PROJECT_ID) and start prompting.

Changes made via Lovable will be committed automatically to this repo.

**Use your preferred IDE**

If you want to work locally using your own IDE, you can clone this repo and push changes. Pushed changes will also be reflected in Lovable.

The only requirement is having Node.js & npm installed - [install with nvm](https://github.com/nvm-sh/nvm#installing-and-updating)

Follow these steps:

```sh
# Step 1: Clone the repository using the project's Git URL.
git clone <YOUR_GIT_URL>

# Step 2: Navigate to the project directory.
cd <YOUR_PROJECT_NAME>

# Step 3: Install the necessary dependencies.
npm i

# Step 4: Start the development server with auto-reloading and an instant preview.
npm run dev
```

**Edit a file directly in GitHub**

- Navigate to the desired file(s).
- Click the "Edit" button (pencil icon) at the top right of the file view.
- Make your changes and commit the changes.

**Use GitHub Codespaces**

- Navigate to the main page of your repository.
- Click on the "Code" button (green button) near the top right.
- Select the "Codespaces" tab.
- Click on "New codespace" to launch a new Codespace environment.
- Edit files directly within the Codespace and commit and push your changes once you're done.

## What technologies are used for this project?

This project is built with:

- Vite
- TypeScript
- React
- shadcn-ui
- Tailwind CSS
- Auth0 (Authentication)

## Auth0 Setup

This project uses Auth0 for authentication. To set up Auth0:

1. **Create an Auth0 Account and Application**
   - Sign up at [auth0.com](https://auth0.com) (free tier available)
   - Go to the Auth0 Dashboard
   - Navigate to Applications → Applications
   - Click "Create Application"
   - Choose "Single Page Application" as the application type
   - Select React as the technology

2. **Configure Auth0 Application Settings**
   - In your Auth0 application settings, configure the following URLs:
     - **Allowed Callback URLs**: `http://localhost:5173`
     - **Allowed Logout URLs**: `http://localhost:5173`
     - **Allowed Web Origins**: `http://localhost:5173`
   - For production, add your production URLs to these fields as well

3. **Create Environment File**
   - Copy `.env.example` to `.env.local`:
     ```sh
     cp .env.example .env.local
     ```
   - Fill in your Auth0 credentials in `.env.local`:
     - `VITE_AUTH0_DOMAIN`: Your Auth0 domain (e.g., `your-tenant.auth0.com`)
     - `VITE_AUTH0_CLIENT_ID`: Your Auth0 Client ID (found in your application settings)
     - `VITE_AUTH0_AUDIENCE`: (Optional) Your API identifier if using Auth0 APIs
     - `VITE_AUTH0_REDIRECT_URI`: `http://localhost:5173` (default)

4. **Start the Development Server**
   ```sh
   npm run dev
   ```

**Note**: The `.env.local` file is git-ignored and will never be committed. Only `.env.example` is tracked in the repository.

## How can I deploy this project?

Simply open [Lovable](https://lovable.dev/projects/REPLACE_WITH_PROJECT_ID) and click on Share -> Publish.

## Can I connect a custom domain to my Lovable project?

Yes, you can!

To connect a domain, navigate to Project > Settings > Domains and click Connect Domain.

Read more here: [Setting up a custom domain](https://docs.lovable.dev/features/custom-domain#custom-domain)
