# Pre-Meeting Intelligence Brief Generator

An AI-powered productivity tool that generates personalized meeting prep cards, helping professionals walk into every meeting with strategic clarity.

Built by **Martha Dixon** for the AWS Builder Center Weekend Challenge (July 2026).

## What It Does

You input a meeting title, the names and roles of attendees and the meeting topic. The tool generates a structured intelligence brief that includes:

- **Attendee Analysis** — What each person likely cares about based on their role and anticipated objections they may raise
- **Tailored Talking Points** — Your strongest arguments for this specific audience
- **The One Question You Must Ask** — A high-value question that demonstrates strategic thinking
- **Recommended Tone & Approach** — Communication style guidance for the room

## Live Demo

**https://jo5sblhcg4rww7tvkdk4zqzm0qmvsb.lambda-url.us-east-1.on.aws**

## Architecture

```
User's Browser
      |
      | HTTPS (GET = page, POST = generate brief)
      v
AWS Lambda (Python 3.12, Function URL)
      |
      | InvokeModel API
      v
Amazon Bedrock (Amazon Nova Lite v1.0)
```

- **AWS Lambda** — Single function serves the frontend (GET) and handles AI generation (POST). No separate hosting needed.
- **Amazon Bedrock** — Nova Lite model provides role-based reasoning and structured text generation.

No API Gateway. No S3. No CORS. One URL does everything.

## How It Works

1. A GET request to the Function URL serves the HTML/CSS/JS frontend
2. The user fills in meeting details and clicks Generate
3. A POST request sends the data to the same Lambda
4. Lambda constructs a prompt and calls Bedrock's Nova Lite model
5. The AI response is returned and rendered as a formatted brief

## Project Structure

```
pre-meeting-brief/
├── lambda_function.py   # Complete application (frontend + backend)
├── README.md            # This file
└── ARTICLE.md           # AWS Builder Center submission article
```

## AWS Services Used

| Service | Purpose |
|---------|---------|
| AWS Lambda | Serves frontend + handles API logic |
| Amazon Bedrock (Nova Lite) | AI-powered brief generation |

## Deploy It Yourself

1. **Create a Lambda function** in the AWS Console (us-east-1 region)
   - Runtime: Python 3.14
   - Architecture: x86_64

2. **Configure the function**
   - Timeout: 60 seconds
   - Memory: 256 MB
   - Add the `AmazonBedrockFullAccess` IAM policy to the function's role

3. **Add the code**
   - Copy the contents of `lambda_function.py` into the Lambda code editor
   - Click Deploy

4. **Create a Function URL**
   - Configuration → Function URL → Create
   - Auth type: NONE
   - That gives you a public URL — open it in your browser and you're live

No additional setup, dependencies or infrastructure needed.

## Builder Info

- **Builder Alias:** BuildWithPurpose
- **Challenge:** AWS Builder Center Weekend Challenge, July 10-13, 2026
- **GitHub:** [MarthaDixon](https://github.com/MarthaDixon)
