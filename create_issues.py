#!/usr/bin/env python3
"""Create GitHub issues from ClubPortalEvent feature comparison."""

import os
import requests
import json

# GitHub API configuration
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
REPO_OWNER = 'KarthikErodeS'
REPO_NAME = 'skills-integrate-mcp-with-copilot'
GITHUB_API_URL = 'https://api.github.com'

# Issue templates based on ClubPortalEvent features
ISSUES = [
    {
        "title": "Feature: Club/Organization Management",
        "body": """Currently, the project has a static list of activities. Implement dynamic club/organization management allowing users to:

- Create new clubs/organizations
- Edit club information and profiles
- Delete clubs
- View all clubs and their members
- Organize clubs in hierarchies

**Reference**: ClubPortalEvent demonstrates this with dedicated club creation and management interfaces.

**Benefits**: More flexible activity management, scalability for multiple organizations."""
    },
    {
        "title": "Feature: User Authentication & Role-Based Access Control",
        "body": """Implement a proper authentication and authorization system with:

- User registration and account creation
- Login/logout functionality
- Role-based access control (Super Admin, Admin, Member)
- Permission management based on roles
- User profile management
- Secure password handling

**Reference**: ClubPortalEvent uses role-based system with different capabilities per role.

**Benefits**: Security, proper data access control, accountability for activities."""
    },
    {
        "title": "Feature: Event Media Gallery & Image Viewer",
        "body": """Add support for event media management:

- Upload event photos and images
- Event photo gallery display
- Full-screen image viewer for event photos
- Image management (delete, organize by event)

**Reference**: ClubPortalEvent includes image gallery and full-screen viewer.

**Benefits**: Enhanced user engagement, better event documentation and memories."""
    },
    {
        "title": "Feature: Financial Management System",
        "body": """Implement financial tracking for clubs and events:

- Track club budgets
- Record financial transactions
- Generate financial reports
- Budget allocation and management
- Transaction history

**Reference**: ClubPortalEvent has comprehensive finance management.

**Benefits**: Better resource management, financial transparency, budget planning."""
    },
    {
        "title": "Feature: Task Management System",
        "body": """Add task management capabilities:

- Create tasks for club members
- Assign tasks to specific members
- Track task progress and status
- Task completion monitoring
- Task assignment notifications

**Reference**: ClubPortalEvent includes dedicated task management.

**Benefits**: Better organization, accountability, improved coordination."""
    },
    {
        "title": "Feature: Data Export to CSV",
        "body": """Implement data export functionality:

- Export activities to CSV
- Export member/participant data to CSV
- Export financial data to CSV
- Export event participation records
- Customizable export fields

**Reference**: ClubPortalEvent includes CsvExportUtils for data export.

**Benefits**: Better reporting, data analysis, integration with other tools."""
    },
    {
        "title": "Feature: Sentiment Analysis for Feedback",
        "body": """Add sentiment analysis for member feedback:

- Collect event feedback/reviews from members
- Analyze sentiment of feedback (positive/negative/neutral)
- Display feedback sentiment dashboard
- Identify improvement areas based on sentiment trends

**Reference**: ClubPortalEvent includes SentimentAnalyzer for feedback analysis.

**Benefits**: Better understanding of member satisfaction, continuous improvement."""
    },
    {
        "title": "Feature: RSS Feed Service",
        "body": """Implement RSS feed functionality:

- Generate RSS feeds for club events
- Activity update feeds
- Member notifications via RSS
- Feed management and customization

**Reference**: ClubPortalEvent includes RssService for activity updates.

**Benefits**: Better engagement, integration with RSS readers and platforms."""
    },
    {
        "title": "Feature: Event Ticketing System",
        "body": """Add event ticketing capabilities:

- Generate tickets for events
- Ticket allocation and management
- Event capacity control via tickets
- Ticket validation and entry management
- Ticket distribution to members

**Reference**: ClubPortalEvent includes Ticket activity for event management.

**Benefits**: Better event capacity management, entry control, attendance tracking."""
    },
    {
        "title": "Feature: Notification System",
        "body": """Implement a comprehensive notification system:

- Notify members about new events
- Task assignment notifications
- Event reminder notifications
- Notification preferences management
- Email/in-app notifications

**Reference**: ClubPortalEvent includes NotificationUtils for member alerts.

**Benefits**: Better member engagement, improved communication."""
    },
    {
        "title": "Feature: Member Profiles & Tracking",
        "body": """Enhance member management with profiles:

- Detailed member profiles with information
- Member activity history tracking
- Member statistics (events attended, tasks completed)
- Member status and role tracking
- Profile customization

**Reference**: ClubPortalEvent tracks member engagement and profiles.

**Benefits**: Better member management, personalized experiences."""
    },
    {
        "title": "Feature: Dark Mode / Theme Support",
        "body": """Add theme customization support:

- Implement dark mode UI
- Light mode as default
- Theme toggle functionality
- Persistent theme preference
- Optimized colors for both themes

**Reference**: ClubPortalEvent includes night mode with dedicated color schemes.

**Benefits**: Better UX for different preferences, reduced eye strain."""
    },
    {
        "title": "Feature: Mobile Responsive Design",
        "body": """Improve mobile responsiveness:

- Responsive layout for mobile devices
- Touch-friendly UI components
- Mobile-optimized navigation
- Adaptive images and content
- Mobile-first design approach

**Reference**: ClubPortalEvent is fully mobile-optimized as Android app.

**Benefits**: Better experience for mobile users, broader accessibility."""
    },
    {
        "title": "Feature: Advanced Event Management",
        "body": """Expand event management capabilities:

- Event scheduling with detailed calendars
- Event categories and types
- Event details and descriptions
- Event date/time management
- Event capacity and registration limits
- Event status tracking

**Reference**: ClubPortalEvent has comprehensive event management (AddEventActivity, ClubEventsActivity).

**Benefits**: More comprehensive event information, better organization."""
    },
    {
        "title": "Feature: Role-Based Dashboards",
        "body": """Implement role-specific dashboards:

- Super Admin dashboard with system overview
- Admin dashboard for club management
- Member dashboard with personal activities
- Different metrics and insights per role
- Customized views based on permissions

**Reference**: ClubPortalEvent includes SuperAdmin activity with role-based views.

**Benefits**: Better user experience, role-appropriate information display."""
    }
]


def create_issue(title, body):
    """Create a single GitHub issue."""
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {GITHUB_TOKEN}',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    
    data = {
        'title': title,
        'body': body
    }
    
    url = f'{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/issues'
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 201:
        issue = response.json()
        print(f"✅ Created issue #{issue['number']}: {title}")
        return issue
    else:
        print(f"❌ Failed to create issue: {title}")
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.text}")
        return None


def main():
    """Create all issues."""
    if not GITHUB_TOKEN:
        print("❌ GITHUB_TOKEN environment variable not set")
        print("Please set your GitHub token: export GITHUB_TOKEN='your_token'")
        return
    
    print(f"🚀 Creating issues in {REPO_OWNER}/{REPO_NAME}...\n")
    
    created = 0
    failed = 0
    
    for issue in ISSUES:
        result = create_issue(issue['title'], issue['body'])
        if result:
            created += 1
        else:
            failed += 1
    
    print(f"\n📊 Summary:")
    print(f"   ✅ Created: {created}")
    print(f"   ❌ Failed: {failed}")


if __name__ == '__main__':
    main()
