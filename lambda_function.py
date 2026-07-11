import json
import boto3

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

def get_html():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pre-Meeting Intelligence Brief</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Playfair+Display:wght@700&family=Open+Sans:wght@400&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Open Sans',sans-serif;background:#F5F0E8;min-height:100vh;color:#2C2C2A;line-height:1.6}
.c{max-width:800px;margin:0 auto;padding:40px 20px}
h1{font-family:'Playfair Display',serif;font-size:2.2rem;color:#4A5C3A;text-align:center;margin-bottom:8px}
.sub{font-family:'Montserrat',sans-serif;color:#7A9068;text-align:center;margin-bottom:40px;font-size:1rem;letter-spacing:0.5px}
.card{background:#ffffff;border:1px solid #E8E2D8;border-radius:12px;padding:32px;margin-bottom:24px;box-shadow:0 2px 12px rgba(74,92,58,0.08)}
.fg{margin-bottom:20px}
label{display:block;font-family:'Montserrat',sans-serif;font-size:.8rem;font-weight:700;color:#3D4A2E;margin-bottom:6px;text-transform:uppercase;letter-spacing:1.5px}
input,textarea{width:100%;padding:12px 16px;background:#F5F0E8;border:1px solid #E8E2D8;border-radius:8px;color:#2C2C2A;font-size:1rem;font-family:'Open Sans',sans-serif}
input:focus,textarea:focus{outline:none;border-color:#7A9068;box-shadow:0 0 0 3px rgba(122,144,104,0.15)}
textarea{resize:vertical;min-height:100px}
.ar{display:flex;gap:12px;margin-bottom:10px;align-items:center}
.ar input{flex:1}
.br{background:rgba(74,92,58,0.1);border:1px solid rgba(74,92,58,0.2);color:#4A5C3A;width:36px;height:36px;border-radius:6px;cursor:pointer;font-size:1.2rem;display:flex;align-items:center;justify-content:center}
.br:hover{background:rgba(74,92,58,0.2)}
.ba{background:rgba(122,144,104,0.08);border:1px dashed #8FA67A;color:#4A5C3A;padding:10px 16px;border-radius:8px;cursor:pointer;font-family:'Montserrat',sans-serif;font-size:.85rem;font-weight:600;width:100%}
.ba:hover{background:rgba(122,144,104,0.15)}
.bg{width:100%;padding:16px;background:linear-gradient(135deg,#4A5C3A,#7A9068);border:none;border-radius:8px;color:#F5F0E8;font-family:'Montserrat',sans-serif;font-size:1.05rem;font-weight:700;cursor:pointer;margin-top:10px;letter-spacing:0.5px;text-transform:uppercase}
.bg:hover{box-shadow:0 4px 20px rgba(74,92,58,0.3);transform:translateY(-1px)}
.bg:disabled{opacity:.6;cursor:not-allowed;transform:none}
#lo{display:none;text-align:center;padding:40px}
.sp{width:40px;height:40px;border:3px solid rgba(122,144,104,0.2);border-top-color:#4A5C3A;border-radius:50%;animation:spin 1s linear infinite;margin:0 auto 16px}
@keyframes spin{to{transform:rotate(360deg)}}
#lo p{color:#7A9068;font-family:'Montserrat',sans-serif}
#re{display:none}
.rh{display:flex;justify-content:space-between;align-items:center;margin-bottom:20px}
.rh h2{font-family:'Playfair Display',serif;font-size:1.4rem;color:#4A5C3A}
.bc{background:rgba(122,144,104,0.1);border:1px solid #8FA67A;color:#4A5C3A;padding:8px 16px;border-radius:6px;cursor:pointer;font-family:'Montserrat',sans-serif;font-size:.8rem;font-weight:600}
.bc:hover{background:rgba(122,144,104,0.2)}
.brief h2{color:#4A5C3A;font-family:'Montserrat',sans-serif;font-size:1.05rem;font-weight:700;margin-top:24px;margin-bottom:12px;padding-bottom:6px;border-bottom:2px solid #8FA67A;text-transform:uppercase;letter-spacing:0.5px}
.brief ul{margin-left:20px;margin-bottom:12px}
.brief li{margin-bottom:8px;color:#2C2C2A}
.brief strong{color:#3D4A2E}
.brief p{margin-bottom:12px}
#er{display:none;background:rgba(180,60,60,0.08);border:1px solid rgba(180,60,60,0.25);border-radius:8px;padding:16px;color:#8B3030;margin-bottom:16px}
.bn{background:rgba(74,92,58,0.08);border:1px solid #8FA67A;color:#4A5C3A;padding:10px 20px;border-radius:6px;cursor:pointer;font-family:'Montserrat',sans-serif;font-weight:600;margin-top:20px}
.bn:hover{background:rgba(74,92,58,0.15)}
footer{text-align:center;margin-top:40px;color:#7A9068;font-family:'Montserrat',sans-serif;font-size:.75rem;letter-spacing:0.5px}
</style>
</head>
<body>
<div class="c">
<h1>Pre-Meeting Intelligence Brief</h1>
<p class="sub">AI-powered meeting prep that gives you the strategic edge</p>
<div id="er"></div>
<div id="fo" class="card">
<div class="fg"><label>Meeting Title</label><input type="text" id="mt" placeholder="e.g., Q3 Roadmap Review"></div>
<div class="fg"><label>Attendees</label><div id="al"><div class="ar"><input type="text" placeholder="Name" class="an"><input type="text" placeholder="Role" class="aro"><button class="br" onclick="rma(this)">&times;</button></div></div><button class="ba" onclick="ada()">+ Add Attendee</button></div>
<div class="fg"><label>Topic / Agenda</label><textarea id="tp" placeholder="What is this meeting about?"></textarea></div>
<button class="bg" id="gb" onclick="gen()">Generate Intelligence Brief</button>
</div>
<div id="lo"><div class="sp"></div><p>Generating your strategic brief...</p></div>
<div id="re"><div class="card"><div class="rh"><h2>Your Intelligence Brief</h2><button class="bc" onclick="cop()">Copy</button></div><div id="brc" class="brief"></div><button class="bn" onclick="res()">Generate Another</button></div></div>
<footer>MARTHA DIXON / CX &amp; AI LEADER | Powered by Amazon Bedrock | AWS Builder Weekend Challenge 2026</footer>
</div>
<script>
function ada(){var l=document.getElementById("al");var r=document.createElement("div");r.className="ar";r.innerHTML='<input type="text" placeholder="Name" class="an"><input type="text" placeholder="Role" class="aro"><button class="br" onclick="rma(this)">&times;</button>';l.appendChild(r)}
function rma(b){if(document.querySelectorAll(".ar").length>1)b.parentElement.remove()}
function gen(){var mt=document.getElementById("mt").value.trim();var tp=document.getElementById("tp").value.trim();var rows=document.querySelectorAll(".ar");var att=[];rows.forEach(function(r){var n=r.querySelector(".an").value.trim();var ro=r.querySelector(".aro").value.trim();if(n&&ro)att.push({name:n,role:ro})});if(!mt||!tp||att.length===0){document.getElementById("er").style.display="block";document.getElementById("er").textContent="Please fill in all fields.";setTimeout(function(){document.getElementById("er").style.display="none"},4000);return}document.getElementById("fo").style.display="none";document.getElementById("lo").style.display="block";document.getElementById("re").style.display="none";fetch(window.location.href,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({meeting_title:mt,attendees:att,topic:tp})}).then(function(r){return r.json()}).then(function(d){if(d.error)throw new Error(d.error);document.getElementById("lo").style.display="none";document.getElementById("re").style.display="block";document.getElementById("brc").innerHTML=md(d.brief)}).catch(function(e){document.getElementById("lo").style.display="none";document.getElementById("fo").style.display="block";document.getElementById("er").style.display="block";document.getElementById("er").textContent="Error: "+e.message;setTimeout(function(){document.getElementById("er").style.display="none"},5000)})}
function res(){document.getElementById("fo").style.display="block";document.getElementById("re").style.display="none"}
function cop(){navigator.clipboard.writeText(document.getElementById("brc").innerText);var b=document.querySelector(".bc");b.textContent="Copied!";setTimeout(function(){b.textContent="Copy"},2000)}
function md(t){var s=String(t);s=s.split("## ").join("SPLITHEADER");var parts=s.split("SPLITHEADER");var out=parts[0];for(var i=1;i<parts.length;i++){var line=parts[i];var nl=line.indexOf("\\n");if(nl===-1)nl=line.length;out+="<h2>"+line.substring(0,nl)+"</h2>"+line.substring(nl)}s=out;s=s.split("**").reduce(function(acc,part,idx){return acc+(idx%2===1?"<strong>"+part+"</strong>":part)},"");s=s.split("\\n- ").join("\\n<li>");s=s.split("\\n\\n").join("<br><br>");s=s.split("\\n").join("<br>");return s}
</script>
</body>
</html>'''


def lambda_handler(event, context):
    method = event.get("requestContext", {}).get("http", {}).get("method", "GET")

    if method == "GET":
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "text/html"},
            "body": get_html()
        }

    try:
        body = json.loads(event.get("body", "{}"))
        meeting_title = body.get("meeting_title", "")
        attendees = body.get("attendees", [])
        topic = body.get("topic", "")

        attendees_formatted = "\n".join(
            f"- {a['name']} - {a['role']}" for a in attendees
        )

        user_prompt = f"""Generate a Pre-Meeting Intelligence Brief for the following meeting:

**Meeting Title:** {meeting_title}

**Attendees:**
{attendees_formatted}

**Topic/Agenda:** {topic}

Generate the brief now."""

        system_prompt = """You are a senior executive communication strategist with 20+ years of experience preparing leaders for high-stakes meetings. You generate Pre-Meeting Intelligence Briefs that are sharp, actionable, and grounded in organizational psychology.

Your output must be structured exactly as follows:

## Attendee Analysis
For each attendee, provide:
- **Name & Role**
- **What they likely care about** (based on their role and typical priorities)
- **Anticipated objections or questions** they may raise

## Your Strongest Talking Points
3-5 tailored talking points for this specific audience, ordered by impact.

## The One Question You Must Ask
A single high-value question that will demonstrate strategic thinking and move the conversation forward.

## Recommended Tone & Approach
A brief paragraph on communication style, pacing, and framing strategy for this meeting.

Rules:
- Be specific to the roles provided, not generic
- Assume a corporate enterprise context unless stated otherwise
- Prioritize actionability over comprehensiveness
- Use confident, direct language appropriate for a senior professional audience
- If the agenda suggests tension or competing priorities, surface that explicitly"""

        response = bedrock.invoke_model(
            modelId="amazon.nova-lite-v1:0",
            contentType="application/json",
            accept="application/json",
            body=json.dumps({
                "inferenceConfig": {
                    "maxTokens": 2048,
                    "temperature": 0.7
                },
                "system": [{"text": system_prompt}],
                "messages": [
                    {"role": "user", "content": [{"text": user_prompt}]}
                ]
            })
        )

        result = json.loads(response["body"].read())
        brief_text = result["output"]["message"]["content"][0]["text"]

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"brief": brief_text})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": str(e)})
        }
