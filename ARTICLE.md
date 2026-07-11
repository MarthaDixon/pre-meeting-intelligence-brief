# Weekend Productivity Challenge: Pre-Meeting Intelligence Brief Generator

**Tag: #productivity**

## Vision & What the App Does

Every professional has walked into a meeting underprepared — unsure what the CFO really cares about, caught off guard by a compliance question or missing the one insight that would have changed the conversation. The Pre-Meeting Intelligence Brief Generator solves this by turning basic meeting details into a strategic prep card in seconds.

Here's how it works: you enter a meeting title, add the names and roles of your attendees and describe the topic or agenda. The tool uses AI to analyze each attendee's likely priorities based on their role, anticipate the objections or questions they'll raise and generate tailored talking points for your specific audience. It also recommends your overall tone and approach and surfaces the single most important question you should ask in that meeting.

This isn't a generic meeting notes tool. It's built for the moment before the meeting — when you need to quickly shift from "I have a meeting in 20 minutes" to "I know exactly how to navigate this room." It's the kind of tool I would use in my own consulting practice, where walking into a room prepared is the difference between delivering value and wasting everyone's time.

The target user is any professional who regularly meets with cross-functional stakeholders — product managers, strategists, consultants or anyone who needs to influence people with different priorities. One click gives you the strategic edge that usually takes 30 minutes of research and mental preparation.

## How You Built It

I built this in a single day during the AWS Builder Weekend Challenge. My key architectural decision was simplicity: I wanted the fewest moving parts possible that would still produce a polished, working product.

**The biggest decision** was putting everything — the frontend HTML and the backend AI logic — into a single Lambda function. When a user visits the URL, the Lambda serves the HTML page. When they submit the form, the same Lambda handles the POST request, calls Bedrock and returns the brief. This eliminated CORS issues entirely and gave me one deployment artifact to manage.

**Challenges I encountered:**

The first challenge was CORS. I initially tried a separate HTML file calling the Lambda Function URL but browser security policies blocked the requests regardless of how I configured the headers. After two failed approaches (configuring Function URL CORS settings, then handling CORS in code), I stepped back and realized I was overcomplicating it. Putting the frontend inside the Lambda itself eliminated the problem entirely.

The second challenge was JavaScript regex inside Python triple-quoted strings. The forward slashes in JavaScript regex literals conflicted with Python's string interpretation, causing syntax errors in the browser. I solved this by replacing all regex operations with simple string split/join methods that don't use special characters.

**Prompt engineering** was where the real product value came from. The system prompt frames the AI as a "senior executive communication strategist" rather than a generic assistant. This produces output that feels like advice from a seasoned consultant — specific to roles, grounded in organizational psychology and structured for quick scanning before walking into a room.

## AWS Services Used / Architecture Overview

The application uses two AWS services:

- **AWS Lambda (Python 3.12)** — Serves the frontend HTML on GET requests and handles AI generation on POST requests. Configured with 256 MB memory and 60-second timeout to accommodate Bedrock response times.

- **Amazon Bedrock (Amazon Nova Lite)** — Powers the AI generation. Nova Lite provides strong reasoning capabilities for role-based analysis while staying within free tier usage for a weekend project.

**Architecture:**

```
User's Browser
      |
      | HTTPS (GET = serve page, POST = generate brief)
      v
AWS Lambda (Function URL)
      |
      | invoke_model API call
      v
Amazon Bedrock (Nova Lite v1.0)
```

The Lambda Function URL provides a public HTTPS endpoint without needing API Gateway, reducing both complexity and cost. The entire application is serverless — there are no servers to manage and costs scale to zero when not in use.

## What You Learned

**Simplicity wins under time pressure.** My instinct was to build a React frontend on Amplify with API Gateway and DynamoDB. That's the "proper" architecture but for a weekend challenge, it would have tripled my setup time. A single Lambda serving both HTML and API responses is unconventional but perfectly functional — and it shipped in hours, not days.

**CORS is still a trap in 2026.** Even with Lambda Function URLs and their built-in CORS configuration, getting browser requests to work from a local file or localhost required more troubleshooting than the actual AI integration. The lesson: if you can avoid cross-origin requests entirely, do it.

**Prompt structure matters more than prompt length.** The difference between a generic brief and a genuinely useful one came down to two things: (1) giving the AI a specific persona with expertise framing and (2) enforcing a rigid output structure. The "Rules" section at the end of the system prompt — especially "be specific to the roles provided, not generic" — dramatically improved output quality.

**Amazon Nova Lite is surprisingly capable.** For role-based reasoning and structured text generation, it produced output comparable to larger models at a fraction of the cost. For a productivity tool that generates meeting prep cards, it's more than sufficient.

**Building tools you'd actually use creates better products.** Because this solves a real problem I face in my consulting work, every design decision was grounded in actual use cases rather than hypothetical requirements. The result is something I'll continue using after the challenge ends.

## Link to App or Repo

**Live Application:** https://jo5sblhcg4rww7tvkdk4zqzm0qmvsb.lambda-url.us-east-1.on.aws

**GitHub Repository:** https://github.com/MarthaDixon/pre-meeting-intelligence-brief
