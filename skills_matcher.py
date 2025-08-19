#!/usr/bin/env python3
"""
Skills Matching System for Sachin Kumar's iOS/macOS Developer Profile
A comprehensive framework for analyzing job descriptions and matching candidate skills.
"""

import re
import json
from typing import Dict, List, Tuple, Set, Optional
from dataclasses import dataclass
from enum import Enum
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from collections import Counter
import difflib

# Download required NLTK data (run once)
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    print("Downloading NLTK data...")
    nltk.download('punkt')
    nltk.download('stopwords')

class SkillCategory(Enum):
    TECHNICAL_CORE = "technical_core"
    TECHNICAL_ADVANCED = "technical_advanced"
    FRAMEWORKS = "frameworks"
    TOOLS = "tools"
    SOFT_SKILLS = "soft_skills"
    DOMAIN_KNOWLEDGE = "domain_knowledge"
    CERTIFICATIONS = "certifications"

class ExperienceLevel(Enum):
    ENTRY = "0-2 years"
    MID = "2-5 years"
    SENIOR = "5-8 years"
    LEAD = "8+ years"

@dataclass
class Skill:
    name: str
    category: SkillCategory
    proficiency: int  # 1-10 scale
    years_experience: float
    keywords: List[str]
    is_critical: bool = False

@dataclass
class JobRequirement:
    skill: str
    category: SkillCategory
    required: bool  # True for must-have, False for nice-to-have
    experience_level: str
    keywords: List[str]
    context: str  # Original text context

@dataclass
class MatchResult:
    job_title: str
    overall_score: float
    category_scores: Dict[SkillCategory, float]
    matched_skills: List[Skill]
    missing_critical_skills: List[str]
    missing_nice_to_have: List[str]
    recommendations: List[str]
    competitive_advantages: List[str]
    interview_focus_areas: List[str]

class SachinProfile:
    """Sachin Kumar's professional profile and skills"""
    
    def __init__(self):
        self.personal_info = {
            "name": "Sachin Kumar",
            "title": "Mac/iOS Developer",
            "experience_years": 2.7,
            "location": "Bangalore, India",
            "email": "sachinmehtab@gmail.com",
            "linkedin": "sachinkumar6174",
            "github": "sachin6174",
            "website": "sachinserver.in"
        }
        
        self.skills = self._initialize_skills()
        self.experience_highlights = self._initialize_experience()
        self.projects = self._initialize_projects()
        
    def _initialize_skills(self) -> List[Skill]:
        """Initialize Sachin's current skill set based on resume"""
        return [
            # Core iOS/macOS Development
            Skill("Swift", SkillCategory.TECHNICAL_CORE, 8, 2.7, 
                  ["swift", "swift programming", "ios swift", "macos swift"], True),
            Skill("iOS Development", SkillCategory.TECHNICAL_CORE, 8, 2.7,
                  ["ios", "ios development", "iphone", "mobile development"], True),
            Skill("macOS Development", SkillCategory.TECHNICAL_CORE, 9, 2.7,
                  ["macos", "mac development", "desktop", "cocoa"], True),
            Skill("Objective-C", SkillCategory.TECHNICAL_CORE, 6, 1.0,
                  ["objective-c", "objective c", "objc"], False),
            
            # Frameworks & UI
            Skill("UIKit", SkillCategory.FRAMEWORKS, 8, 2.7,
                  ["uikit", "ui kit", "ios ui", "interface"], True),
            Skill("SwiftUI", SkillCategory.FRAMEWORKS, 8, 2.7,
                  ["swiftui", "swift ui", "declarative ui"], True),
            Skill("Core Data", SkillCategory.FRAMEWORKS, 8, 2.7,
                  ["core data", "coredata", "data persistence"], True),
            
            # Architecture & Patterns
            Skill("MVC/MVVM", SkillCategory.TECHNICAL_ADVANCED, 7, 2.0,
                  ["mvc", "mvvm", "architecture", "design patterns"], False),
            
            # Development Tools
            Skill("Xcode", SkillCategory.TOOLS, 8, 2.7,
                  ["xcode", "ide", "development environment"], True),
            Skill("Git", SkillCategory.TOOLS, 7, 2.7,
                  ["git", "github", "gitlab", "version control"], True),
            
            # Testing
            Skill("XCTest", SkillCategory.TECHNICAL_ADVANCED, 6, 1.5,
                  ["xctest", "unit testing", "testing"], False),
            Skill("XCUITest", SkillCategory.TECHNICAL_ADVANCED, 6, 1.5,
                  ["xcuitest", "ui testing", "automation"], False),
            
            # System Integration
            Skill("Shell Scripting", SkillCategory.TECHNICAL_ADVANCED, 7, 2.0,
                  ["shell", "bash", "scripting", "automation"], False),
            Skill("Command Line Tools", SkillCategory.TECHNICAL_ADVANCED, 8, 2.0,
                  ["command line", "cli", "terminal"], False),
            Skill("XPC Communication", SkillCategory.TECHNICAL_ADVANCED, 8, 2.0,
                  ["xpc", "inter-process", "communication"], False),
            Skill("Process Management", SkillCategory.TECHNICAL_ADVANCED, 7, 2.0,
                  ["daemon", "process", "agent", "background"], False),
            
            # Networking & Security
            Skill("Network Extensions", SkillCategory.TECHNICAL_ADVANCED, 6, 1.0,
                  ["network extension", "vpn", "networking"], False),
            Skill("APNs", SkillCategory.TECHNICAL_ADVANCED, 7, 1.5,
                  ["apns", "push notifications", "remote notifications"], False),
            Skill("Keychain", SkillCategory.TECHNICAL_ADVANCED, 7, 2.0,
                  ["keychain", "security", "credentials"], False),
            
            # Web Technologies
            Skill("React", SkillCategory.TECHNICAL_CORE, 6, 1.0,
                  ["react", "reactjs", "web development"], False),
            Skill("Node.js", SkillCategory.TECHNICAL_CORE, 6, 1.0,
                  ["node", "nodejs", "backend", "javascript"], False),
            
            # Databases
            Skill("SQL", SkillCategory.TECHNICAL_CORE, 6, 1.5,
                  ["sql", "database", "queries"], False),
            Skill("MongoDB", SkillCategory.TECHNICAL_CORE, 5, 1.0,
                  ["mongodb", "nosql", "document database"], False),
            
            # Domain Knowledge
            Skill("MDM (Mobile Device Management)", SkillCategory.DOMAIN_KNOWLEDGE, 9, 2.0,
                  ["mdm", "device management", "suremdm", "enterprise"], True),
            Skill("Enterprise iOS/macOS", SkillCategory.DOMAIN_KNOWLEDGE, 8, 2.0,
                  ["enterprise", "business", "corporate"], False),
            
            # Soft Skills
            Skill("Problem Solving", SkillCategory.SOFT_SKILLS, 8, 2.7,
                  ["problem solving", "debugging", "troubleshooting"], False),
            Skill("Team Collaboration", SkillCategory.SOFT_SKILLS, 7, 2.7,
                  ["collaboration", "teamwork", "communication"], False),
        ]
    
    def _initialize_experience(self) -> List[Dict]:
        """Initialize key experience highlights"""
        return [
            {
                "role": "Mac/iOS Developer",
                "company": "42 Gears Mobility Systems",
                "duration": "July 2023 - Current",
                "key_achievements": [
                    "Developed app management jobs (PKG, DMG installation/upgrade/uninstall)",
                    "Implemented file transfer systems and geofencing with reverse geocoding",
                    "Built device monitoring (uptime, hardware changes) and user management",
                    "Created analytics collection for device events and app usage",
                    "Resolved issues in network extensions, QR enrollment, log encryption"
                ]
            },
            {
                "role": "Mac/iOS Developer Intern",
                "company": "42 Gears Mobility Systems",
                "duration": "February 2023 - June 2023",
                "key_achievements": [
                    "Learned Swift, UIKit, SwiftUI, and asynchronous programming",
                    "Gained expertise in PKG/DMG creation, signing, notarization",
                    "Developed skills in macOS scripting and code quality tools"
                ]
            }
        ]
    
    def _initialize_projects(self) -> List[Dict]:
        """Initialize personal projects"""
        return [
            {
                "name": "NotingDown",
                "description": "SwiftUI and Core Data note-taking app on Apple App Store",
                "technologies": ["SwiftUI", "Core Data", "iOS"],
                "link": "https://github.com/sachin6174/NotingDown"
            },
            {
                "name": "Secure Text",
                "description": "Chrome extension for text encryption/decryption with Base64/Base32 encoding",
                "technologies": ["JavaScript", "Chrome Extension", "Encryption"],
                "link": "https://github.com/sachin6174/SecureText"
            },
            {
                "name": "QR Encoder Decoder",
                "description": "Chrome extension for password-based text encryption with QR code generation",
                "technologies": ["JavaScript", "Chrome Extension", "QR Code", "Encryption"],
                "link": "https://github.com/sachin6174/QREncoderDecoder"
            }
        ]

class JobDescriptionAnalyzer:
    """Analyzes job descriptions and extracts requirements"""
    
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.ios_skill_patterns = self._initialize_skill_patterns()
        self.experience_patterns = self._initialize_experience_patterns()
        
    def _initialize_skill_patterns(self) -> Dict[str, List[str]]:
        """Define patterns for recognizing iOS/macOS skills"""
        return {
            # Core iOS/macOS
            "Swift": ["swift", "swift programming", "swift language"],
            "Objective-C": ["objective-c", "objective c", "objc", "obj-c"],
            "iOS": ["ios", "ios development", "iphone", "mobile ios"],
            "macOS": ["macos", "mac os", "osx", "os x", "mac development"],
            
            # Frameworks
            "UIKit": ["uikit", "ui kit"],
            "SwiftUI": ["swiftui", "swift ui", "declarative ui"],
            "Core Data": ["core data", "coredata"],
            "Core Animation": ["core animation", "coreanimation"],
            "AVFoundation": ["avfoundation", "av foundation"],
            "CloudKit": ["cloudkit", "cloud kit"],
            "Core Location": ["core location", "corelocation"],
            "MapKit": ["mapkit", "map kit"],
            "HealthKit": ["healthkit", "health kit"],
            "HomeKit": ["homekit", "home kit"],
            "SiriKit": ["sirikit", "siri kit"],
            "ARKit": ["arkit", "ar kit", "augmented reality"],
            "RealityKit": ["realitykit", "reality kit"],
            "Combine": ["combine", "reactive programming"],
            "Cocoa": ["cocoa", "cocoa touch"],
            "Foundation": ["foundation framework"],
            
            # Architecture & Patterns
            "MVC": ["mvc", "model view controller"],
            "MVVM": ["mvvm", "model view viewmodel"],
            "MVP": ["mvp", "model view presenter"],
            "VIPER": ["viper architecture"],
            "Clean Architecture": ["clean architecture"],
            "Redux": ["redux", "redux pattern"],
            
            # Development Tools
            "Xcode": ["xcode", "xcode ide"],
            "Interface Builder": ["interface builder", "ib", "storyboard"],
            "Instruments": ["instruments", "xcode instruments", "profiling"],
            "TestFlight": ["testflight", "test flight"],
            "App Store Connect": ["app store connect", "itunes connect"],
            
            # Testing
            "XCTest": ["xctest", "xc test"],
            "XCUITest": ["xcuitest", "xcui test", "ui testing"],
            "Quick": ["quick framework"],
            "Nimble": ["nimble framework"],
            "Snapshot Testing": ["snapshot testing"],
            
            # Networking
            "URLSession": ["urlsession", "url session"],
            "Alamofire": ["alamofire"],
            "Networking": ["networking", "rest api", "json"],
            "GraphQL": ["graphql", "graph ql"],
            
            # Database & Persistence
            "SQLite": ["sqlite", "sql lite"],
            "Realm": ["realm database", "realm swift"],
            "UserDefaults": ["userdefaults", "user defaults"],
            "Keychain": ["keychain", "keychain services"],
            "File System": ["file system", "file manager"],
            
            # Concurrency
            "Grand Central Dispatch": ["gcd", "grand central dispatch"],
            "Operation Queue": ["operation queue", "nsoperation"],
            "Async/Await": ["async await", "async/await", "concurrency"],
            
            # Memory Management
            "ARC": ["arc", "automatic reference counting"],
            "Memory Management": ["memory management", "retain", "release"],
            
            # Security
            "Keychain Services": ["keychain services"],
            "Biometric Authentication": ["touch id", "face id", "biometric"],
            "App Transport Security": ["ats", "app transport security"],
            
            # Distribution & Deployment
            "App Store": ["app store", "app store review"],
            "Enterprise Distribution": ["enterprise distribution", "in-house"],
            "Ad Hoc Distribution": ["ad hoc", "adhoc"],
            "Code Signing": ["code signing", "provisioning profile"],
            "Fastlane": ["fastlane", "automation"],
            
            # Version Control
            "Git": ["git", "github", "gitlab", "bitbucket"],
            "SVN": ["svn", "subversion"],
            
            # CI/CD
            "Jenkins": ["jenkins"],
            "GitHub Actions": ["github actions"],
            "Bitrise": ["bitrise"],
            "CircleCI": ["circleci", "circle ci"],
            
            # Cross-Platform
            "React Native": ["react native", "reactnative"],
            "Flutter": ["flutter", "dart"],
            "Xamarin": ["xamarin"],
            "Cordova": ["cordova", "phonegap"],
            
            # Backend Integration
            "Firebase": ["firebase"],
            "AWS": ["aws", "amazon web services"],
            "Google Cloud": ["google cloud", "gcp"],
            "Azure": ["azure", "microsoft azure"],
            
            # Soft Skills
            "Agile": ["agile", "scrum", "kanban"],
            "Problem Solving": ["problem solving", "debugging"],
            "Communication": ["communication", "teamwork"],
            "Leadership": ["leadership", "mentoring"],
        }
    
    def _initialize_experience_patterns(self) -> List[Tuple[str, str]]:
        """Patterns for detecting experience requirements"""
        return [
            (r"(\d+)\+?\s*years?\s*(?:of\s*)?(?:experience|exp)", "years"),
            (r"(\d+)-(\d+)\s*years?\s*(?:of\s*)?(?:experience|exp)", "range"),
            (r"minimum\s*(\d+)\s*years?", "minimum"),
            (r"at least\s*(\d+)\s*years?", "minimum"),
            (r"senior", "senior"),
            (r"lead", "lead"),
            (r"principal", "principal"),
            (r"junior", "junior"),
            (r"entry.level", "entry"),
            (r"mid.level", "mid"),
        ]
    
    def analyze_job_description(self, job_text: str, job_title: str = "") -> List[JobRequirement]:
        """Analyze job description and extract requirements"""
        requirements = []
        
        # Clean and tokenize text
        clean_text = self._clean_text(job_text)
        sentences = sent_tokenize(clean_text)
        
        # Extract skills with context
        for sentence in sentences:
            sentence_lower = sentence.lower()
            
            # Check for each skill pattern
            for skill, patterns in self.ios_skill_patterns.items():
                for pattern in patterns:
                    if pattern in sentence_lower:
                        # Determine if required or nice-to-have
                        is_required = self._is_skill_required(sentence_lower)
                        
                        # Extract experience level
                        exp_level = self._extract_experience_level(sentence_lower)
                        
                        # Determine category
                        category = self._categorize_skill(skill)
                        
                        requirement = JobRequirement(
                            skill=skill,
                            category=category,
                            required=is_required,
                            experience_level=exp_level,
                            keywords=patterns,
                            context=sentence
                        )
                        requirements.append(requirement)
                        break
        
        # Remove duplicates and sort by importance
        unique_requirements = self._deduplicate_requirements(requirements)
        return sorted(unique_requirements, key=lambda x: (x.required, x.skill))
    
    def _clean_text(self, text: str) -> str:
        """Clean and normalize text"""
        # Remove extra whitespace and normalize
        text = re.sub(r'\s+', ' ', text.strip())
        # Remove special characters but keep important punctuation
        text = re.sub(r'[^\w\s\.\,\-\+\(\)]', ' ', text)
        return text
    
    def _is_skill_required(self, sentence: str) -> bool:
        """Determine if skill is required or nice-to-have"""
        required_indicators = [
            "required", "must have", "essential", "mandatory", "critical",
            "necessary", "needed", "should have", "minimum", "at least"
        ]
        nice_to_have_indicators = [
            "nice to have", "preferred", "bonus", "plus", "advantage",
            "desirable", "would be great", "ideal", "appreciated"
        ]
        
        sentence_lower = sentence.lower()
        
        # Check for nice-to-have indicators first (more specific)
        for indicator in nice_to_have_indicators:
            if indicator in sentence_lower:
                return False
        
        # Check for required indicators
        for indicator in required_indicators:
            if indicator in sentence_lower:
                return True
        
        # Default to required if unclear
        return True
    
    def _extract_experience_level(self, sentence: str) -> str:
        """Extract experience level requirements"""
        for pattern, level_type in self.experience_patterns:
            match = re.search(pattern, sentence, re.IGNORECASE)
            if match:
                if level_type == "years":
                    years = int(match.group(1))
                    return f"{years}+ years"
                elif level_type == "range":
                    min_years = int(match.group(1))
                    max_years = int(match.group(2))
                    return f"{min_years}-{max_years} years"
                elif level_type == "minimum":
                    years = int(match.group(1))
                    return f"{years}+ years"
                else:
                    return level_type
        return "Not specified"
    
    def _categorize_skill(self, skill: str) -> SkillCategory:
        """Categorize skills based on type"""
        core_skills = ["Swift", "Objective-C", "iOS", "macOS"]
        frameworks = ["UIKit", "SwiftUI", "Core Data", "Core Animation", "Combine"]
        tools = ["Xcode", "Instruments", "Git", "Fastlane"]
        advanced = ["MVC", "MVVM", "XCTest", "Networking", "Memory Management"]
        
        if skill in core_skills:
            return SkillCategory.TECHNICAL_CORE
        elif skill in frameworks:
            return SkillCategory.FRAMEWORKS
        elif skill in tools:
            return SkillCategory.TOOLS
        elif skill in advanced:
            return SkillCategory.TECHNICAL_ADVANCED
        else:
            return SkillCategory.TECHNICAL_ADVANCED
    
    def _deduplicate_requirements(self, requirements: List[JobRequirement]) -> List[JobRequirement]:
        """Remove duplicate requirements"""
        seen_skills = set()
        unique_requirements = []
        
        for req in requirements:
            if req.skill not in seen_skills:
                seen_skills.add(req.skill)
                unique_requirements.append(req)
        
        return unique_requirements

class SkillsMatcher:
    """Main skills matching engine"""
    
    def __init__(self, profile: SachinProfile):
        self.profile = profile
        self.analyzer = JobDescriptionAnalyzer()
        
    def match_job(self, job_description: str, job_title: str = "iOS/macOS Developer") -> MatchResult:
        """Match profile against job requirements"""
        
        # Analyze job requirements
        job_requirements = self.analyzer.analyze_job_description(job_description, job_title)
        
        # Calculate matches
        matched_skills = []
        missing_critical = []
        missing_nice_to_have = []
        category_scores = {}
        
        # Create skill lookup for faster matching
        profile_skills_dict = {skill.name.lower(): skill for skill in self.profile.skills}
        profile_keywords = {}
        for skill in self.profile.skills:
            for keyword in skill.keywords:
                profile_keywords[keyword.lower()] = skill
        
        # Match each requirement
        for req in job_requirements:
            matched = False
            
            # Direct skill name match
            if req.skill.lower() in profile_skills_dict:
                matched_skills.append(profile_skills_dict[req.skill.lower()])
                matched = True
            else:
                # Try keyword matching
                for keyword in req.keywords:
                    if keyword.lower() in profile_keywords:
                        matched_skills.append(profile_keywords[keyword.lower()])
                        matched = True
                        break
            
            # Track missing skills
            if not matched:
                if req.required:
                    missing_critical.append(req.skill)
                else:
                    missing_nice_to_have.append(req.skill)
        
        # Calculate category scores
        requirements_by_category = {}
        matches_by_category = {}
        
        for req in job_requirements:
            if req.category not in requirements_by_category:
                requirements_by_category[req.category] = 0
                matches_by_category[req.category] = 0
            requirements_by_category[req.category] += 1
        
        for skill in matched_skills:
            if skill.category in matches_by_category:
                matches_by_category[skill.category] += 1
        
        for category in requirements_by_category:
            if requirements_by_category[category] > 0:
                category_scores[category] = (matches_by_category.get(category, 0) / 
                                           requirements_by_category[category]) * 100
            else:
                category_scores[category] = 100
        
        # Calculate overall score
        total_requirements = len(job_requirements)
        total_matches = len(matched_skills)
        overall_score = (total_matches / total_requirements * 100) if total_requirements > 0 else 100
        
        # Generate recommendations
        recommendations = self._generate_recommendations(missing_critical, missing_nice_to_have, job_requirements)
        
        # Identify competitive advantages
        competitive_advantages = self._identify_competitive_advantages(matched_skills)
        
        # Generate interview focus areas
        interview_focus = self._generate_interview_focus(matched_skills, missing_critical)
        
        return MatchResult(
            job_title=job_title,
            overall_score=overall_score,
            category_scores=category_scores,
            matched_skills=list(set(matched_skills)),  # Remove duplicates
            missing_critical_skills=missing_critical,
            missing_nice_to_have=missing_nice_to_have,
            recommendations=recommendations,
            competitive_advantages=competitive_advantages,
            interview_focus_areas=interview_focus
        )
    
    def _generate_recommendations(self, missing_critical: List[str], 
                                missing_nice_to_have: List[str], 
                                job_requirements: List[JobRequirement]) -> List[str]:
        """Generate learning and improvement recommendations"""
        recommendations = []
        
        if missing_critical:
            recommendations.append(f"🚨 CRITICAL: Learn these skills immediately: {', '.join(missing_critical[:3])}")
            
            # Provide specific learning suggestions
            for skill in missing_critical[:5]:
                if skill.lower() in ["combine", "async/await"]:
                    recommendations.append(f"📚 {skill}: Take Apple's official documentation course (2-3 weeks)")
                elif skill.lower() in ["arkit", "realitykit"]:
                    recommendations.append(f"📚 {skill}: Build AR project following Apple tutorials (1 month)")
                elif skill.lower() in ["cloudkit", "firebase"]:
                    recommendations.append(f"📚 {skill}: Integrate into existing NotingDown app (2 weeks)")
                else:
                    recommendations.append(f"📚 {skill}: Add to learning priority (timeline varies)")
        
        if missing_nice_to_have:
            recommendations.append(f"💡 NICE-TO-HAVE: Consider learning: {', '.join(missing_nice_to_have[:3])}")
        
        # Experience-based recommendations
        experience_levels = [req.experience_level for req in job_requirements if "years" in req.experience_level]
        if experience_levels:
            max_required = max([int(re.search(r'(\d+)', exp).group(1)) for exp in experience_levels if re.search(r'(\d+)', exp)])
            if max_required > self.profile.personal_info["experience_years"]:
                recommendations.append(f"⏱️ Experience gap: Role asks for {max_required}+ years, you have {self.profile.personal_info['experience_years']}. Emphasize depth of MDM experience.")
        
        return recommendations
    
    def _identify_competitive_advantages(self, matched_skills: List[Skill]) -> List[str]:
        """Identify unique strengths that set candidate apart"""
        advantages = []
        
        # Check for unique combinations
        skill_names = [skill.name.lower() for skill in matched_skills]
        
        if "mdm (mobile device management)" in [skill.name.lower() for skill in self.profile.skills]:
            advantages.append("🏆 Specialized MDM expertise - rare combination with 2.7 years hands-on experience")
        
        if all(skill in skill_names for skill in ["swift", "swiftui", "core data"]):
            advantages.append("🎯 Modern iOS stack mastery - SwiftUI + Core Data combination")
        
        if "xpc communication" in skill_names:
            advantages.append("⚡ Advanced system integration skills - XPC communication expertise")
        
        if "shell scripting" in skill_names and "command line tools" in skill_names:
            advantages.append("🔧 Strong automation skills - Shell scripting + CLI tools")
        
        # Check for high proficiency skills
        high_proficiency = [skill for skill in matched_skills if skill.proficiency >= 8]
        if high_proficiency:
            advantages.append(f"💪 Expert-level skills: {', '.join([skill.name for skill in high_proficiency[:3]])}")
        
        # Check for published apps
        if any("app store" in proj["description"].lower() for proj in self.profile.projects):
            advantages.append("📱 Published App Store developer - proven shipping experience")
        
        return advantages
    
    def _generate_interview_focus(self, matched_skills: List[Skill], missing_critical: List[str]) -> List[str]:
        """Generate interview preparation focus areas"""
        focus_areas = []
        
        # Focus on strongest skills
        strongest_skills = sorted(matched_skills, key=lambda x: x.proficiency, reverse=True)[:5]
        if strongest_skills:
            focus_areas.append(f"💪 Emphasize expertise in: {', '.join([skill.name for skill in strongest_skills])}")
        
        # Prepare for missing critical skills
        if missing_critical:
            focus_areas.append(f"🎯 Prepare explanations for: {', '.join(missing_critical[:3])} - show learning plan")
        
        # Specific technical areas
        if any("core data" in skill.name.lower() for skill in matched_skills):
            focus_areas.append("📊 Prepare Core Data questions: relationships, migrations, performance")
        
        if any("swiftui" in skill.name.lower() for skill in matched_skills):
            focus_areas.append("🎨 SwiftUI deep dive: state management, custom views, animations")
        
        # Experience-based focus
        focus_areas.append("🏢 MDM domain expertise: SureMDM experience, enterprise challenges")
        focus_areas.append("📱 Published app discussion: NotingDown architecture, challenges, learnings")
        
        return focus_areas

class ResumeCustomizer:
    """Provides resume customization suggestions"""
    
    def __init__(self, profile: SachinProfile):
        self.profile = profile
    
    def generate_custom_keywords(self, job_requirements: List[JobRequirement]) -> Dict[str, List[str]]:
        """Generate keywords to add for specific job"""
        keyword_suggestions = {
            "skills_section": [],
            "experience_bullets": [],
            "project_descriptions": []
        }
        
        # Extract required skills not prominently featured
        required_skills = [req.skill for req in job_requirements if req.required]
        
        for skill in required_skills:
            # Check if skill exists but could be emphasized more
            if skill.lower() in ["combine", "async/await", "concurrency"]:
                keyword_suggestions["experience_bullets"].append(
                    f"Add: 'Implemented asynchronous programming using {skill} for optimized performance'"
                )
            elif skill.lower() in ["unit testing", "xctest"]:
                keyword_suggestions["experience_bullets"].append(
                    "Add: 'Developed comprehensive unit tests ensuring 90%+ code coverage'"
                )
        
        return keyword_suggestions
    
    def suggest_experience_modifications(self, match_result: MatchResult) -> List[str]:
        """Suggest modifications to experience bullet points"""
        suggestions = []
        
        # If missing testing skills
        if any("test" in skill.lower() for skill in match_result.missing_critical_skills):
            suggestions.append(
                "🔄 Modify: 'Resolved issues in network extensions...' → "
                "'Developed and tested network extensions with comprehensive unit test coverage...'"
            )
        
        # If missing specific frameworks
        if "Combine" in match_result.missing_critical_skills:
            suggestions.append(
                "🔄 Add: 'Implemented reactive programming patterns for data flow optimization'"
            )
        
        # Emphasize relevant experience
        if match_result.overall_score < 70:
            suggestions.append(
                "📈 Emphasize: Expand on most relevant technical achievements in current role"
            )
        
        return suggestions

def main():
    """Demonstration of the skills matching system"""
    
    # Initialize profile and matcher
    profile = SachinProfile()
    matcher = SkillsMatcher(profile)
    customizer = ResumeCustomizer(profile)
    
    # Example job description
    sample_job = """
    Senior iOS Developer
    
    We are looking for a Senior iOS Developer to join our team. 
    
    Required Skills:
    - 5+ years of iOS development experience
    - Expert knowledge of Swift and SwiftUI
    - Experience with Core Data and CloudKit
    - Strong understanding of iOS design patterns (MVVM, MVC)
    - Experience with unit testing (XCTest) and UI testing
    - Proficient with Xcode and version control (Git)
    - Experience with Combine framework for reactive programming
    - Knowledge of ARKit for augmented reality features
    
    Nice to have:
    - Experience with CI/CD pipelines
    - Knowledge of backend technologies
    - Published apps on the App Store
    - Experience with Fastlane for automation
    """
    
    # Analyze the job
    print("🔍 ANALYZING JOB DESCRIPTION...")
    print("=" * 50)
    
    match_result = matcher.match_job(sample_job, "Senior iOS Developer")
    
    # Display results
    print(f"📊 OVERALL MATCH SCORE: {match_result.overall_score:.1f}%")
    print("\n📈 CATEGORY SCORES:")
    for category, score in match_result.category_scores.items():
        print(f"  {category.value}: {score:.1f}%")
    
    print(f"\n✅ MATCHED SKILLS ({len(match_result.matched_skills)}):")
    for skill in match_result.matched_skills[:10]:  # Show top 10
        print(f"  • {skill.name} (Proficiency: {skill.proficiency}/10)")
    
    if match_result.missing_critical_skills:
        print(f"\n🚨 MISSING CRITICAL SKILLS ({len(match_result.missing_critical_skills)}):")
        for skill in match_result.missing_critical_skills:
            print(f"  • {skill}")
    
    if match_result.missing_nice_to_have:
        print(f"\n💡 MISSING NICE-TO-HAVE ({len(match_result.missing_nice_to_have)}):")
        for skill in match_result.missing_nice_to_have[:5]:
            print(f"  • {skill}")
    
    print("\n🎯 RECOMMENDATIONS:")
    for rec in match_result.recommendations:
        print(f"  {rec}")
    
    print("\n🏆 COMPETITIVE ADVANTAGES:")
    for adv in match_result.competitive_advantages:
        print(f"  {adv}")
    
    print("\n🎤 INTERVIEW FOCUS AREAS:")
    for focus in match_result.interview_focus_areas:
        print(f"  {focus}")
    
    # Resume customization suggestions
    job_requirements = matcher.analyzer.analyze_job_description(sample_job)
    keywords = customizer.generate_custom_keywords(job_requirements)
    modifications = customizer.suggest_experience_modifications(match_result)
    
    print("\n📝 RESUME CUSTOMIZATION:")
    if modifications:
        for mod in modifications:
            print(f"  {mod}")
    
    print("\n" + "=" * 50)
    print("Skills matching analysis complete!")

if __name__ == "__main__":
    main()