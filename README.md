# LinEscalate
LinEscalate automates Linux security checks, swiftly identifying vulnerabilities and enhancing system resilience against potential threats. Ideal for both seasoned users and newcomers to security assessment.

## Features

- **Automated Security Checks**: LinEscalate automates the process of identifying security issues, saving time and effort for both experienced Linux users and newcomers to security assessment.
- **Comprehensive Analysis**: LinEscalate provides a comprehensive analysis of various aspects of the system, including system information, user permissions, sensitive files, SUID/SGID files, and more.
- **Color-Coded Output**: The output is color-coded for easy identification of potential risks, with cyan for section titles, yellow for potential vulnerabilities, and red for definite vulnerabilities.
- **Educational Use**: LinEscalate is intended for educational purposes and initial security assessments, helping users learn about Linux security and proactively address security concerns.

## Usage

1. **Clone the repository**: `git clone https://github.com/PixelPlatypus/LinEscalate.git`
2. **Navigate to the LinEscalate directory**: `cd LinEscalate`
3. **Run the script**: `python LinEscalate.py`
4. **Follow the on-screen instructions**: Select specific checks or run a full scan to analyze the output for potential security issues.

## Color Coding

- **Cyan**: Section titles for easy navigation.
- **Yellow**: Indicates potential vulnerabilities. For example, contents of sensitive files, SUID/SGID files.
- **Red**: Highlights definite vulnerabilities. For instance, world-writable files, writable PATH directories, and known vulnerable kernel versions.

## Disclaimer

Use LinEscalate responsibly and ensure appropriate permissions before running it on any system. While LinEscalate can aid in identifying potential security vulnerabilities, it is not a substitute for thorough security auditing or professional security assessments.

## Contributing

Contributions are welcome! If you have any ideas for improvements, feel free to open an issue or submit a pull request.

