# SquadBid - Group Buying Platform

A simple and modern group buying platform where users can create deals and join others to unlock better discounts. This project demonstrates a real-time group buying experience with features like countdown timers, progress tracking, and dynamic participant updates.

## Features

- **Create Group Deals**
  - Set product name, description, and pricing
  - Define minimum participant requirements
  - Set time limits for deals
  - Specify discount percentages

- **Join Active Deals**
  - View all active group deals
  - Real-time progress tracking
  - Time remaining countdown
  - Easy join process with name and email

- **Real-time Updates**
  - Live participant count updates
  - Dynamic progress bars
  - Automatic deal expiration
  - Status updates every 30 seconds

## Tech Stack

- **Backend**
  - FastAPI (Python web framework)
  - SQLite (Database)
  - SQLAlchemy (ORM)
  - Pydantic (Data validation)

- **Frontend**
  - HTML/CSS/JavaScript
  - Bootstrap 5 (UI framework)
  - Custom CSS animations
  - Real-time updates via JavaScript

## Setup Instructions

1. **Install Python Dependencies**
   ```bash
   pip install fastapi uvicorn jinja2 python-multipart sqlalchemy
   ```

2. **Run the Application**
   ```bash
   cd group_buy
   uvicorn app.main:app --reload
   ```

3. **Access the Application**
   - Open your browser and navigate to `http://127.0.0.1:8000`
   - The application will automatically create the SQLite database on first run

## Project Structure

```
group_buy/
├── app/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── script.js
│   ├── templates/
│   │   └── index.html
│   ├── models.py
│   ├── database.py
│   └── main.py
└── README.md
```

## How to Use

1. **Creating a Deal**
   - Fill out the "Create New Group Deal" form on the left
   - Provide product details, pricing, and requirements
   - Set the time limit for the deal

2. **Joining a Deal**
   - Browse active deals on the right side
   - Click "Join Deal" on any active deal
   - Enter your name and email
   - Watch the progress bar update

3. **Monitoring Deals**
   - Progress bars show current participant count
   - Countdown timers show remaining time
   - Deals automatically expire when time runs out
   - Join buttons disable for expired deals

## Known Limitations

- No user authentication system
- No persistent session management
- Simple email validation without verification
- No payment integration
- Local SQLite database (not suitable for production)

## Future Improvements

- User authentication and accounts
- Email verification system
- Payment gateway integration
- More sophisticated deal options
- Admin dashboard
- Deal categories and search
- Social sharing features

## Contributing

This is a demonstration project for the SquadBid internship task. Feel free to fork and modify for your own use.

## License

This project is created as part of the SquadBid internship task and is intended for demonstration purposes. 