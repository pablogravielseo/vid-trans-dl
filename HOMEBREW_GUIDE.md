# Publishing vid-trans-dl to Homebrew

This guide explains how to publish the vid-trans-dl tool as a Homebrew package.

## Prerequisites

1. A GitHub account
2. Your project hosted on GitHub
3. Git installed on your machine
4. Homebrew installed on your machine

## Step 1: Prepare Your Project for Release

1. Make sure your project is properly versioned (e.g., v0.1.0)
2. Create a GitHub repository for your project if you haven't already
3. Push your code to GitHub
4. Create a release/tag on GitHub (e.g., v0.1.0)

## Step 2: Calculate the SHA256 Hash

After creating a release on GitHub, you need to calculate the SHA256 hash of the source tarball:

```bash
# Replace with your actual GitHub username and release version
curl -L https://github.com/pablogravielseo/vid-trans-dl/archive/refs/tags/v0.1.0.tar.gz | shasum -a 256
```

## Step 3: Update the Formula

1. Update the `url` in the formula to point to your actual GitHub repository
2. Replace `REPLACE_WITH_ACTUAL_SHA256_AFTER_RELEASE` with the SHA256 hash you calculated
3. Update the `homepage` to point to your actual GitHub repository
4. Update the resource URLs and SHA256 hashes for dependencies if needed

## Step 4: Test the Formula Locally

```bash
# Create a directory for your tap
mkdir -p $(brew --repo)/Library/Taps/pablogravielseo/homebrew-tools

# Copy your formula to the tap
cp Formula/vid-trans-dl.rb $(brew --repo)/Library/Taps/pablogravielseo/homebrew-tools/

# Install the formula
brew install --build-from-source pablogravielseo/tools/vid-trans-dl
```

## Step 5: Create a Homebrew Tap Repository

1. Create a new GitHub repository named `homebrew-tools` (the prefix `homebrew-` is required)
2. Add your formula to this repository:

```bash
mkdir -p homebrew-tools/Formula
cp Formula/vid-trans-dl.rb homebrew-tools/Formula/
cd homebrew-tools
git init
git add .
git commit -m "Add vid-trans-dl formula"
git remote add origin https://github.com/pablogravielseo/homebrew-tools.git
git push -u origin main
```

## Step 6: Install from Your Tap

Now users can install your package using:

```bash
brew tap pablogravielseo/tools
brew install vid-trans-dl
```

## Step 7 (Optional): Submit to Homebrew Core

If you want your formula to be included in the main Homebrew repository:

1. Fork the [Homebrew/homebrew-core](https://github.com/Homebrew/homebrew-core) repository
2. Add your formula to the `Formula` directory
3. Submit a pull request

Note that Homebrew has strict requirements for packages in the core repository, including:
- The software must be maintained and stable
- It should be open-source with an acceptable license
- It should have a certain level of popularity or usefulness

## Updating Your Formula

When you release a new version:

1. Update the version number in the formula
2. Calculate the new SHA256 hash
3. Update the formula in your tap repository
4. Commit and push the changes

## Resources

- [Homebrew Formula Cookbook](https://docs.brew.sh/Formula-Cookbook)
- [Homebrew Tap Guide](https://docs.brew.sh/How-to-Create-and-Maintain-a-Tap)
- [Python for Formula Authors](https://docs.brew.sh/Python-for-Formula-Authors) 