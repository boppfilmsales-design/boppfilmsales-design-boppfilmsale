import os
import re

folder = r"C:\Users\DELL\Desktop\files"
files = [f for f in os.listdir(folder) if f.endswith('.html')]

removed = 0
for filename in files:
    filepath = os.path.join(folder, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove all chatbot-related HTML
    content = re.sub(r'<div id="chatbot-[^"]*">.*?</div>\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'<div id="chatbot-[^"]*">\s*', '', content)
    content = re.sub(r'</div>\s*', '</div>', content)

    # Remove all chatbot-related CSS
    content = re.sub(r'#chatbot-[^}]*\}\s*', '', content)
    content = re.sub(r'\.chatbot-[^}]*\}\s*', '', content)
    content = re.sub(r'#chatbot-[^}]*\{[^}]*\}\s*', '', content)

    # Remove chatbot JavaScript
    content = re.sub(r'function toggleChat\(\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function handleKeyPress\([^)]*\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function sendChatMessage\(\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function addChatMessage\([^)]*\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function showToast\([^)]*\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function scrollToBottom\(\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function askQuestion\([^)]*\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function closeChat\(\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function openChat\(\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function toggleChatbot\(\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function initChatbot\(\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function togglePanel\(\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function closePanel\(\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function openPanel\(\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function toggleContact\(\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function closeContact\(\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function openContact\(\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function toggleWhyUs\(\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function closeWhyUs\(\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function openWhyUs\(\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function toggleSpecs\(\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function closeSpecs\(\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function openSpecs\(\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function toggleApps\(\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function closeApps\(\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function openApps\(\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function toggleContact\(\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function closeContact\(\)\{[^}]*\}\s*', '', content)
    content = re.sub(r'function openContact\(\)\{[^}]*\}\s*', '', content)

    # Remove empty style tags
    content = re.sub(r'<style>\s*</style>\s*', '', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    removed += 1
    print(f"Removed chatbot from: {filename}")

print(f"\nTotal files updated: {removed}")
