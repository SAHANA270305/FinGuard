# Allerguard
OpenFoodFacts API
1. Define the Scope
Since you’re a beginner, focus on building a Minimum Viable Product (MVP) with one or two core features. For example:

A mobile app that lets users input allergens and scan food labels to detect potential allergens.

A basic pollen/allergy alert system using public APIs.

2. Plan the Core Features
Pick 1-3 simple features to start with:

User Input System: Allow users to input their allergens (e.g., peanuts, gluten, dairy).

Barcode/Label Scanner: Use a simple scanner to analyze food products for allergens.

Alert Notifications: Notify users if a scanned product contains allergens or if pollen levels are high.

3. Technology Stack
Select beginner-friendly tools to simplify development:

Frontend (User Interface):

Use HTML/CSS/JavaScript for a web app.

Use Flutter (Dart) or React Native for a mobile app (if time permits).

If focusing on Android, start with Android Studio (Java/Kotlin).

Backend (Processing and Logic):

Use Python (Flask) or Node.js for basic backend tasks.

Database:

Use a simple database like Firebase for storing user allergen data or profiles.

APIs:

OpenFoodFacts API: For food and allergen data.

OpenWeatherMap API: For pollen or air quality data.

4. Step-by-Step Development Plan
Step 1: Design User Flow
User Journey: Sketch out how users will interact with the app.

Input allergens → Scan product → Receive alerts.

Input location → View allergy risk in the area.

Use tools like Figma or even paper sketches to visualize screens.

Step 2: Create the User Interface
Build basic screens:

Welcome Screen: Brief intro to the app.

Profile Screen: Let users enter allergens.

Scanner Screen: Include a button to scan food labels (or simulate with a text box)

Alert Screen: Show notifications for detected allergens or environmental risks.

Step 3: Integrate APIs
Start with an API to pull real-world data.

For food allergens: Use OpenFoodFacts API.

For environmental data: Use OpenWeatherMap API.

Test API calls using tools like Postman before integrating them into your app.

Step 4: Build Core Logic
Write functions to:

Match user-input allergens with API data.

Trigger notifications if allergens are detected.

Fetch environmental data and display pollen levels.

Step 5: Add Simple Alerts
Use a basic notification system:

For web: Use browser notifications with JavaScript.

For mobile: Use a push notification service like Firebase Cloud Messaging (FCM).

Step 6: Test and Debug
Test your app with sample data.

Check:

Are allergens correctly detected?

Are alerts timely and clear?

Is the interface easy to navigate?

Example User Flow for Allergy Alert System
Here’s how your Figma flow could look:

Welcome Screen: "Start" → Button: Get Started
→ Leads to the Profile Screen.

Profile Screen: User adds allergen list → Button: Save & Continue
→ Leads to the Scan Product Screen.

Scan Product Screen: Upload or scan label → Button: Analyze
→ Leads to the Result Screen.

Result Screen: Displays allergen warning or confirmation → Button: Back to Home.

