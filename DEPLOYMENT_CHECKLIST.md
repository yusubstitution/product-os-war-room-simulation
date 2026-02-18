# Streamlit Dashboard Deployment Checklist

## Pre-Deployment: Test Locally

```bash
# 1. Navigate to project folder
cd /Users/jyu/Documents/20\ -\ Claude\ Code\ Projects/product-os-war-room-simulation

# 2. Activate virtual environment
source venv/bin/activate

# 3. Run dashboard
streamlit run app.py

# 4. Test in browser at http://localhost:8501
# - Click through all 5 tabs
# - Verify charts load correctly
# - Check that data tables display properly
# - Confirm key findings are visible:
#   - Tab 2: Mobile 51% abandonment vs Desktop 28%
#   - Tab 3: Event Cloning 247 tickets in Q4
#   - Tab 4: Analytics users 95% retention vs 73%

# 5. Stop server (Ctrl+C)
```

---

## Deployment to Streamlit Cloud

### Step 1: Create GitHub Repository

```bash
# Initialize git (if not already done)
cd product-os-war-room-simulation
git init

# Create .gitignore (already done)
# Make sure these are ignored:
# - venv/
# - __pycache__/
# - *.pyc

# Stage files (don't commit master-features-list.md!)
git add app.py
git add generate_data.py
git add requirements.txt
git add data/*.csv
git add role-packets/engineering-lead-packet.md
git add role-packets/sales-lead-packet.md
git add role-packets/tpm-packet-instructions.md
git add company-profile.md
git add README.md
git add .gitignore

# Commit
git commit -m "Add Product OS War Room simulation dashboard"

# Create repo on GitHub:
# - Go to https://github.com/new
# - Name: product-os-war-room-simulation
# - Private or Public (Public is fine, it's fake data)
# - Don't initialize with README (we have one)

# Push to GitHub
git remote add origin https://github.com/YOUR_USERNAME/product-os-war-room-simulation.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Streamlit Cloud

1. Go to https://share.streamlit.io/ (or https://streamlit.io/cloud)

2. Sign in with your GitHub account

3. Click "New app" button

4. Fill in deployment settings:
   - **Repository:** YOUR_USERNAME/product-os-war-room-simulation
   - **Branch:** main
   - **Main file path:** app.py
   - **App URL** (optional): Choose a custom subdomain or use default

5. Click "Deploy!"

6. Wait 2-3 minutes for deployment (watch the logs)

7. Once deployed, you'll get a URL like:
   ```
   https://YOUR_USERNAME-product-os-war-room-simulation-app-xxxxxx.streamlit.app
   ```

8. **Test the deployed app:**
   - Click through all tabs
   - Verify data loads correctly
   - Check that charts render properly

### Step 3: Share URL

- Copy the Streamlit app URL
- Update `role-packets/tpm-packet-instructions.md` with the URL
- Print TPM instructions for the simulation

---

## Troubleshooting

### Dashboard won't load locally

```bash
# Check virtual environment is activated
which python
# Should show: .../venv/bin/python

# Reinstall dependencies
pip install -r requirements.txt

# Check data files exist
ls data/
# Should show 4 CSV files
```

### Deployment fails on Streamlit Cloud

**Error: "ModuleNotFoundError"**
- Check that `requirements.txt` is committed to GitHub
- Verify all imports in `app.py` are in requirements.txt

**Error: "FileNotFoundError: data/..."**
- Make sure `data/` folder and CSVs are committed to GitHub
- Check file paths are relative (not absolute)

**Charts not rendering**
- Check Streamlit Cloud logs for errors
- Verify plotly is in requirements.txt

### Data looks wrong

```bash
# Regenerate synthetic data
source venv/bin/activate
python generate_data.py

# Verify files were created
ls -lh data/
```

---

## Before the Offsite

- [ ] Dashboard deployed to Streamlit Cloud
- [ ] URL tested and working
- [ ] TPM instructions updated with dashboard URL
- [ ] Engineering Lead packets printed (6-7 copies)
- [ ] Sales Lead packets printed (6-7 copies)
- [ ] TPM instructions printed (6-7 copies)
- [ ] Laptops/tablets available for TPMs to access dashboard
- [ ] Team worksheets printed
- [ ] Facilitator guide prepared
- [ ] Answer key (master-features-list.md) ready for debrief

---

## Day-of Simulation Checklist

1. **Before session starts:**
   - [ ] Test dashboard URL on venue WiFi
   - [ ] Confirm laptops/tablets can access dashboard
   - [ ] Have printed packets organized by role
   - [ ] Team worksheets and pens ready
   - [ ] Answer key prepared for debrief

2. **During setup (5 min):**
   - [ ] Divide TPMs into teams of 3
   - [ ] Assign roles (Engineering, Sales, TPM)
   - [ ] Distribute role packets
   - [ ] Give TPMs dashboard URL (write on whiteboard or share via Slack)

3. **After simulation:**
   - [ ] Collect team worksheets
   - [ ] Calculate ARR for each team's selections
   - [ ] Prepare debrief slides showing optimal vs actual

---

## Post-Offsite

- [ ] Gather feedback from TPMs
- [ ] Save team worksheets for documentation
- [ ] Consider keeping dashboard live for future demos
- [ ] Update simulation materials based on feedback

---

## Questions?

Contact: Jason Yu (jyu@abnormalsecurity.com)
