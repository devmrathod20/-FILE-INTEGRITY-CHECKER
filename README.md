# -FILE-INTEGRITY-CHECKER

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: DEV MANISHKUMAR RATHOD

*INTERN ID*: CT04DH2886

*DOMAIN*: CYBER SECURITY AND ETHICAL HACKING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

*DESCRIPTION*:

For my first task in the Cyber Security & Ethical Hacking internship, I built a simple yet practical tool called a File Integrity Checker. The main idea behind this tool is to help detect any unauthorized or accidental changes to important files by using hash values.

In the world of cyber security, file integrity plays a big role in protecting systems from tampering and corruption. Even a tiny change in a file — like a single character — can completely change its hash value. That’s why this tool uses the SHA-256 hashing algorithm, which is a secure and reliable way to create a unique “fingerprint” for a file.

How it works:
The tool is a Python script that does two main things:

Generate & store the file hash:
First, the user can add or update a file’s hash. The script reads the file, calculates its hash value, and saves it in a simple JSON file called hashes.json. This saved hash acts like the file’s original signature.

Check for changes:
Later, whenever we want to check if the file is still the same, the script recalculates its hash and compares it with the stored one. If they match, the file is unchanged. If not, the tool warns the user that the file may have been modified.

Why this matters:
This task taught me how even basic tools can help improve security. Hackers often try to change system files or scripts to introduce vulnerabilities. With a file integrity checker, such changes can be detected early. It’s like having a security guard that regularly checks if anything has been tampered with.

I also learned how to use Python’s hashlib library, how to read and write JSON data, and how to handle files in binary mode. All of this helped me improve my practical coding skills and understand how cryptographic hash functions work in real life.

Key highlights:

Uses SHA-256 hashing for strong file integrity checking.

Stores hashes neatly in a JSON file for easy management.

Provides a simple menu for adding or checking file hashes.

Keeps users informed with clear, friendly messages.

My takeaway:
I really enjoyed working on this task because it showed me how a small script can add real security value. It’s straightforward but gives a clear picture of how organizations keep their files safe from unauthorized changes. This also motivated me to think about how more advanced integrity monitoring tools are built in the industry.

Overall, this task gave me practical experience in using Python for security automation — and I’m excited to apply this knowledge to bigger tools in the coming tasks!

*OUTPUT*:

<img width="1914" height="998" alt="Image" src="https://github.com/user-attachments/assets/dec0aa92-17b7-4d7c-9523-e582c1823879" />
