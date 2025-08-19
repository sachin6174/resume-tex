#!/usr/bin/env python3
"""
Sample Job Descriptions for Testing the Skills Matching System
Includes various iOS/macOS developer roles at different levels and companies
"""

SAMPLE_JOBS = {
    "senior_ios_developer": {
        "title": "Senior iOS Developer - Tech Startup",
        "company": "TechFlow Inc.",
        "description": """
        We are seeking a Senior iOS Developer to join our growing team and help build the next generation of mobile experiences.

        Requirements:
        • 5+ years of iOS development experience
        • Expert proficiency in Swift and modern iOS frameworks
        • Strong experience with SwiftUI and UIKit
        • Deep understanding of iOS architecture patterns (MVVM, MVC)
        • Experience with Core Data and CloudKit
        • Proficient in unit testing with XCTest and UI testing
        • Experience with Combine framework for reactive programming
        • Knowledge of iOS security best practices
        • Experience with Git version control and collaborative development

        Nice to have:
        • Experience with ARKit/RealityKit
        • Knowledge of CI/CD pipelines (Fastlane, GitHub Actions)
        • Backend development experience
        • Published apps on the App Store
        • Experience with performance optimization and Instruments

        We offer competitive salary, equity, and the opportunity to work on cutting-edge technology.
        """
    },
    
    "ios_engineer_faang": {
        "title": "iOS Software Engineer - Meta",
        "company": "Meta (Facebook)",
        "description": """
        Meta is looking for iOS Engineers to help build apps that connect billions of people worldwide.

        Minimum Qualifications:
        • Bachelor's degree in Computer Science or equivalent practical experience
        • 3+ years of software development experience with iOS
        • Experience with Swift and Objective-C
        • Strong understanding of iOS SDK, Xcode, and development tools
        • Experience with multi-threading, memory management, and performance optimization
        • Knowledge of software engineering best practices

        Preferred Qualifications:
        • 5+ years of iOS development experience
        • Experience building large-scale consumer applications
        • Knowledge of accessibility features and internationalization
        • Experience with A/B testing and experimentation platforms
        • Understanding of network protocols and RESTful APIs
        • Experience with GraphQL
        • Knowledge of iOS app distribution and App Store review process
        • Experience mentoring junior developers

        At Meta, you'll work on products used by billions and have access to cutting-edge technology and resources.
        """
    },
    
    "junior_ios_developer": {
        "title": "Junior iOS Developer - FinTech",
        "company": "FinanceApp Solutions",
        "description": """
        Join our FinTech team as a Junior iOS Developer and help build secure financial applications.

        Requirements:
        • 1-3 years of iOS development experience
        • Knowledge of Swift and basic iOS development concepts
        • Familiarity with UIKit and basic SwiftUI
        • Understanding of MVC architecture pattern
        • Basic knowledge of Core Data or similar persistence frameworks
        • Experience with Xcode and Interface Builder
        • Understanding of version control (Git)

        Nice to have:
        • Knowledge of financial/banking domain
        • Experience with security frameworks and encryption
        • Familiarity with unit testing
        • Understanding of Agile development methodologies
        • Knowledge of RESTful web services

        We provide mentorship, training opportunities, and a path for career growth in a dynamic FinTech environment.
        """
    },
    
    "lead_ios_architect": {
        "title": "Lead iOS Architect - Enterprise",
        "company": "Enterprise Solutions Corp",
        "description": """
        We're seeking a Lead iOS Architect to design and oversee iOS solutions for enterprise clients.

        Requirements:
        • 8+ years of iOS development experience
        • 3+ years in architectural/lead roles
        • Expert knowledge of Swift, Objective-C, and iOS frameworks
        • Deep understanding of iOS design patterns and architectural principles
        • Experience with enterprise iOS deployment and MDM solutions
        • Strong knowledge of iOS security, encryption, and compliance requirements
        • Experience with CI/CD, automated testing, and DevOps practices
        • Leadership experience and ability to mentor development teams
        • Excellent communication skills for client interactions

        Technical Requirements:
        • Advanced knowledge of Core Data, CloudKit, and enterprise databases
        • Experience with network security, VPN, and enterprise networking
        • Knowledge of iOS app distribution methods (App Store, Enterprise, Ad Hoc)
        • Experience with code signing, provisioning profiles, and certificates
        • Understanding of accessibility requirements and compliance standards

        Preferred:
        • Experience with Mobile Device Management (MDM) platforms
        • Knowledge of enterprise authentication systems (Active Directory, SAML, OAuth)
        • Experience with cross-platform development strategies
        • Industry certifications in iOS development or security

        This role offers the opportunity to shape iOS strategy for major enterprise clients and lead a team of talented developers.
        """
    },
    
    "ios_developer_healthcare": {
        "title": "iOS Developer - Healthcare Technology",
        "company": "HealthTech Innovations",
        "description": """
        Join our mission to revolutionize healthcare through technology as an iOS Developer.

        Required Skills:
        • 3-5 years of iOS development experience
        • Proficiency in Swift and iOS SDK
        • Experience with HealthKit and health data integration
        • Knowledge of HIPAA compliance and healthcare data security
        • Experience with Core Data and data persistence
        • Understanding of medical device integration and Bluetooth LE
        • Familiarity with FDA regulations for medical software

        Technical Requirements:
        • SwiftUI and UIKit proficiency
        • Experience with RESTful APIs and JSON parsing
        • Knowledge of encryption and secure data handling
        • Unit testing and quality assurance practices
        • Experience with app store submission and review process

        Preferred Qualifications:
        • Background in healthcare, medical devices, or life sciences
        • Experience with machine learning frameworks for health applications
        • Knowledge of interoperability standards (FHIR, HL7)
        • Experience with real-time data processing and notifications
        • Understanding of accessibility requirements for healthcare apps

        Make a difference in people's lives while working with cutting-edge healthcare technology.
        """
    },
    
    "macos_developer_enterprise": {
        "title": "macOS Developer - Enterprise Management",
        "company": "DeviceManagement Pro",
        "description": """
        We're looking for a macOS Developer to build next-generation enterprise device management solutions.

        Core Requirements:
        • 4+ years of macOS development experience
        • Expert knowledge of Swift and Objective-C for macOS
        • Deep understanding of macOS system architecture and frameworks
        • Experience with Cocoa and AppKit frameworks
        • Knowledge of macOS security model and sandboxing
        • Experience with command-line tools and shell scripting
        • Understanding of macOS deployment and packaging (PKG, DMG)

        Enterprise Focus:
        • Experience with Mobile Device Management (MDM) for macOS
        • Knowledge of Apple Business Manager and Apple School Manager
        • Understanding of macOS configuration profiles and restrictions
        • Experience with enterprise authentication and directory services
        • Knowledge of macOS deployment tools and automation
        • Understanding of compliance requirements and audit trails

        Technical Skills:
        • XPC and inter-process communication
        • Launch daemons and agents
        • System extensions and kernel extensions (deprecated)
        • Code signing and notarization
        • Network programming and security protocols
        • Database integration and data synchronization

        This role offers the opportunity to work on systems that manage thousands of enterprise Mac devices worldwide.
        """
    },
    
    "ios_contractor_remote": {
        "title": "iOS Developer - Contract/Remote",
        "company": "Digital Agency Collective",
        "description": """
        We're seeking experienced iOS developers for various client projects on a contract basis.

        Project Types:
        • E-commerce and retail applications
        • Social media and communication apps
        • Productivity and utility applications
        • Entertainment and media streaming apps

        Technical Requirements:
        • 3+ years of iOS development experience
        • Strong portfolio of published iOS applications
        • Proficiency in Swift and modern iOS development practices
        • Experience with various iOS frameworks (UIKit, SwiftUI, Core Data, etc.)
        • Ability to work independently and meet project deadlines
        • Strong communication skills for remote collaboration

        Current Project Needs:
        • SwiftUI expertise for modern UI development
        • Core Data and CloudKit integration
        • Push notifications and real-time features
        • In-app purchases and subscription management
        • Social media SDK integration
        • Performance optimization and debugging

        Ideal for:
        • Experienced developers seeking flexible work arrangements
        • Those looking to work on diverse projects and technologies
        • Developers wanting to build relationships with multiple clients

        Competitive hourly rates and long-term project opportunities available.
        """
    }
}

def get_sample_job(job_key: str) -> dict:
    """Get a specific sample job by key"""
    return SAMPLE_JOBS.get(job_key)

def list_sample_jobs() -> list:
    """List all available sample job keys"""
    return list(SAMPLE_JOBS.keys())

def get_all_sample_jobs() -> dict:
    """Get all sample jobs"""
    return SAMPLE_JOBS

def demo_analysis():
    """Run demo analysis on all sample jobs"""
    from job_analyzer import JobAnalyzer
    
    print("🎯 RUNNING DEMO ANALYSIS ON SAMPLE JOBS")
    print("=" * 60)
    
    analyzer = JobAnalyzer()
    results = []
    
    for job_key, job_data in SAMPLE_JOBS.items():
        print(f"\n📋 Analyzing: {job_data['title']}")
        print("-" * 40)
        
        result = analyzer.analyze_job_from_text(
            job_data['description'], 
            job_data['title']
        )
        results.append(result)
        
        # Brief summary
        print(f"Match Score: {result.overall_score:.1f}%")
        print(f"Critical Gaps: {len(result.missing_critical_skills)}")
        print(f"Advantages: {len(result.competitive_advantages)}")
    
    # Compare all jobs
    print(f"\n🔄 COMPARING ALL {len(results)} JOBS")
    print("=" * 60)
    analyzer.compare_jobs(results)
    
    return results

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--demo":
            demo_analysis()
        elif sys.argv[1] == "--list":
            print("Available sample jobs:")
            for i, job_key in enumerate(list_sample_jobs(), 1):
                job = get_sample_job(job_key)
                print(f"{i:2d}. {job_key}: {job['title']}")
        elif sys.argv[1] in SAMPLE_JOBS:
            job = get_sample_job(sys.argv[1])
            print(f"Title: {job['title']}")
            print(f"Company: {job['company']}")
            print("\nDescription:")
            print(job['description'])
        else:
            print(f"Job '{sys.argv[1]}' not found. Use --list to see available jobs.")
    else:
        print("Usage:")
        print("  python sample_jobs.py --demo          # Run analysis on all sample jobs")
        print("  python sample_jobs.py --list          # List all sample jobs")
        print("  python sample_jobs.py <job_key>       # Show specific job description")