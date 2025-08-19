#!/usr/bin/env python3
"""
Complete Demonstration of Sachin Kumar's Skills Matching System
Shows all features and capabilities with real examples
"""

import sys
from skills_matcher import SachinProfile, SkillsMatcher, ResumeCustomizer
from job_analyzer import JobAnalyzer
from sample_jobs import get_sample_job, list_sample_jobs

def print_header(title: str, char: str = "="):
    """Print a formatted header"""
    print(f"\n{char * 60}")
    print(f"{title:^60}")
    print(f"{char * 60}")

def print_section(title: str):
    """Print a section header"""
    print(f"\n{'─' * 50}")
    print(f"📋 {title}")
    print(f"{'─' * 50}")

def demo_profile_overview():
    """Demonstrate profile overview functionality"""
    print_header("👨‍💻 SACHIN KUMAR - PROFILE OVERVIEW")
    
    profile = SachinProfile()
    analyzer = JobAnalyzer()
    analyzer.show_profile_summary()

def demo_single_job_analysis():
    """Demonstrate single job analysis"""
    print_header("🔍 SINGLE JOB ANALYSIS DEMO")
    
    # Use a realistic job description
    job = get_sample_job("senior_ios_developer")
    analyzer = JobAnalyzer()
    
    print(f"Analyzing: {job['title']}")
    print(f"Company: {job['company']}")
    
    result = analyzer.analyze_job_from_text(job['description'], job['title'])
    return result

def demo_multiple_job_comparison():
    """Demonstrate comparing multiple jobs"""
    print_header("🔄 MULTIPLE JOB COMPARISON DEMO")
    
    analyzer = JobAnalyzer()
    results = []
    
    # Analyze 3 different types of jobs
    job_keys = ['junior_ios_developer', 'senior_ios_developer', 'lead_ios_architect']
    
    for job_key in job_keys:
        job = get_sample_job(job_key)
        print(f"\n📱 Analyzing: {job['title']}")
        
        result = analyzer.analyze_job_from_text(job['description'], job['title'])
        results.append(result)
        
        # Show brief summary
        print(f"   Match Score: {result.overall_score:.1f}%")
        print(f"   Critical Gaps: {len(result.missing_critical_skills)}")
    
    # Compare all jobs
    print_section("JOB COMPARISON RESULTS")
    analyzer.compare_jobs(results)
    
    return results

def demo_resume_customization():
    """Demonstrate resume customization suggestions"""
    print_header("📝 RESUME CUSTOMIZATION DEMO")
    
    profile = SachinProfile()
    matcher = SkillsMatcher(profile)
    customizer = ResumeCustomizer(profile)
    
    # Analyze a job that has some gaps
    job = get_sample_job("ios_engineer_faang")
    result = matcher.match_job(job['description'], job['title'])
    
    print(f"📊 Customization for: {job['title']}")
    print(f"Current Match Score: {result.overall_score:.1f}%")
    
    # Get customization suggestions
    job_requirements = matcher.analyzer.analyze_job_description(job['description'])
    keywords = customizer.generate_custom_keywords(job_requirements)
    modifications = customizer.suggest_experience_modifications(result)
    
    print_section("RESUME CUSTOMIZATION SUGGESTIONS")
    
    if modifications:
        print("🔧 Experience Modifications:")
        for mod in modifications:
            print(f"  {mod}")
    else:
        print("✅ Current experience bullets are well-aligned!")
    
    print("\n💡 Keyword Enhancement Opportunities:")
    if any(keywords.values()):
        for section, suggestions in keywords.items():
            if suggestions:
                print(f"  {section.replace('_', ' ').title()}:")
                for suggestion in suggestions:
                    print(f"    • {suggestion}")
    else:
        print("  Current keywords are comprehensive for this role!")

def demo_competitive_analysis():
    """Demonstrate competitive analysis features"""
    print_header("🏆 COMPETITIVE ANALYSIS DEMO")
    
    profile = SachinProfile()
    matcher = SkillsMatcher(profile)
    
    # Analyze different job types to show competitive positioning
    job_types = [
        ('junior_ios_developer', 'Junior Level'),
        ('senior_ios_developer', 'Senior Level'),
        ('macos_developer_enterprise', 'Enterprise macOS'),
    ]
    
    for job_key, level_desc in job_types:
        job = get_sample_job(job_key)
        result = matcher.match_job(job['description'], job['title'])
        
        print(f"\n📊 {level_desc} Position:")
        print(f"   Match Score: {result.overall_score:.1f}%")
        print(f"   Competitive Advantages: {len(result.competitive_advantages)}")
        
        if result.competitive_advantages:
            for advantage in result.competitive_advantages[:2]:  # Show top 2
                print(f"   • {advantage}")

def demo_learning_roadmap():
    """Demonstrate learning roadmap generation"""
    print_header("🎯 LEARNING ROADMAP DEMO")
    
    analyzer = JobAnalyzer()
    
    # Analyze a challenging senior role
    job = get_sample_job("lead_ios_architect")
    result = analyzer.analyze_job_from_text(job['description'], job['title'])
    
    print(f"📚 Learning Roadmap for: {job['title']}")
    print(f"Current Match: {result.overall_score:.1f}%")
    
    # Organize missing skills by priority
    critical_skills = result.missing_critical_skills
    nice_to_have = result.missing_nice_to_have
    
    print_section("LEARNING PRIORITIES")
    
    if critical_skills:
        print("🚨 IMMEDIATE PRIORITIES (Critical Skills):")
        for i, skill in enumerate(critical_skills[:5], 1):
            # Provide realistic timelines
            if any(keyword in skill.lower() for keyword in ['leadership', 'architect', 'lead']):
                timeline = "6-12 months (experience-based)"
            elif any(keyword in skill.lower() for keyword in ['security', 'compliance', 'enterprise']):
                timeline = "2-3 months (certification + projects)"
            else:
                timeline = "3-6 weeks (hands-on learning)"
            
            print(f"  {i}. {skill} - {timeline}")
    
    if nice_to_have:
        print(f"\n💡 SECONDARY PRIORITIES (Nice-to-have):")
        for i, skill in enumerate(nice_to_have[:3], 1):
            print(f"  {i}. {skill}")
    
    print_section("RECOMMENDED LEARNING PATH")
    print("1. 📱 Short-term (1-3 months):")
    print("   • Focus on critical technical skills with immediate impact")
    print("   • Build portfolio projects demonstrating new capabilities")
    print("   • Contribute to open-source projects")
    
    print("\n2. 🎯 Medium-term (3-6 months):")
    print("   • Gain leadership experience through mentoring or leading features")
    print("   • Obtain relevant certifications")
    print("   • Attend conferences and networking events")
    
    print("\n3. 🚀 Long-term (6-12 months):")
    print("   • Take on architectural responsibilities in current role")
    print("   • Build reputation through blogging/speaking")
    print("   • Apply for target senior positions")

def demo_application_strategy():
    """Demonstrate application strategy recommendations"""
    print_header("📋 APPLICATION STRATEGY DEMO")
    
    analyzer = JobAnalyzer()
    
    # Analyze jobs with different match scores
    strategies = []
    
    jobs_to_analyze = [
        ('junior_ios_developer', 'High Match Expected'),
        ('senior_ios_developer', 'Medium Match Expected'),
        ('lead_ios_architect', 'Low Match Expected')
    ]
    
    for job_key, expectation in jobs_to_analyze:
        job = get_sample_job(job_key)
        result = analyzer.analyze_job_from_text(job['description'], job['title'])
        strategies.append((job['title'], result.overall_score, result))
    
    print_section("APPLICATION PRIORITY MATRIX")
    
    # Sort by match score
    strategies.sort(key=lambda x: x[1], reverse=True)
    
    for i, (title, score, result) in enumerate(strategies, 1):
        priority = "HIGH" if score >= 75 else "MEDIUM" if score >= 60 else "LOW"
        emoji = "🟢" if score >= 75 else "🟡" if score >= 60 else "🔴"
        
        print(f"{emoji} {i}. {title}")
        print(f"     Match: {score:.1f}% | Priority: {priority}")
        
        if score >= 75:
            print(f"     🚀 Action: Apply immediately")
            print(f"     ⏱️ Timeline: Expect response within 1-2 weeks")
        elif score >= 60:
            print(f"     📚 Action: 1-2 weeks preparation, then apply")
            print(f"     🎯 Focus: Address {len(result.missing_critical_skills)} critical gaps")
        else:
            print(f"     ⏳ Action: Long-term target (2-3 months preparation)")
            print(f"     📖 Focus: Major skill development needed")
        
        print()

def demo_export_functionality():
    """Demonstrate export and save functionality"""
    print_header("💾 EXPORT & SAVE DEMO")
    
    analyzer = JobAnalyzer()
    
    # Analyze a job
    job = get_sample_job("senior_ios_developer")
    result = analyzer.analyze_job_from_text(job['description'], job['title'])
    
    # Save analysis
    filename = "demo_analysis_results.json"
    analyzer.save_analysis(result, filename)
    
    print(f"✅ Analysis saved to: {filename}")
    print("📄 Contains:")
    print("  • Complete match analysis")
    print("  • Skill breakdown by category")
    print("  • Learning recommendations")
    print("  • Competitive advantages")
    print("  • Interview preparation tips")

def interactive_demo():
    """Run an interactive demo"""
    print_header("🎮 INTERACTIVE DEMO MODE")
    
    demos = [
        ("Profile Overview", demo_profile_overview),
        ("Single Job Analysis", demo_single_job_analysis),
        ("Multiple Job Comparison", demo_multiple_job_comparison),
        ("Resume Customization", demo_resume_customization),
        ("Competitive Analysis", demo_competitive_analysis),
        ("Learning Roadmap", demo_learning_roadmap),
        ("Application Strategy", demo_application_strategy),
        ("Export Functionality", demo_export_functionality),
    ]
    
    print("Available demonstrations:")
    for i, (name, _) in enumerate(demos, 1):
        print(f"  {i}. {name}")
    print(f"  {len(demos) + 1}. Run All Demos")
    print(f"  0. Exit")
    
    while True:
        try:
            choice = int(input(f"\nSelect demo (0-{len(demos) + 1}): "))
            
            if choice == 0:
                print("👋 Demo complete! Explore the system with real job descriptions.")
                break
            elif choice == len(demos) + 1:
                print("🚀 Running all demonstrations...")
                for name, demo_func in demos:
                    print(f"\n⏳ Running: {name}")
                    demo_func()
                    input("\nPress Enter to continue to next demo...")
                break
            elif 1 <= choice <= len(demos):
                name, demo_func = demos[choice - 1]
                print(f"\n⏳ Running: {name}")
                demo_func()
                input("\nPress Enter to return to menu...")
            else:
                print("❌ Invalid choice. Please try again.")
        
        except (ValueError, KeyboardInterrupt):
            print("\n👋 Demo interrupted. Goodbye!")
            break

def main():
    """Main demo entry point"""
    print("🎯 SACHIN'S SKILLS MATCHING SYSTEM - COMPLETE DEMO")
    print("=" * 60)
    print("This demo showcases all features of the comprehensive skills matching system.")
    print("The system analyzes job descriptions and provides detailed matching analysis,")
    print("learning recommendations, and application strategies.")
    
    if len(sys.argv) > 1:
        demo_type = sys.argv[1].lower()
        
        if demo_type == "profile":
            demo_profile_overview()
        elif demo_type == "analysis":
            demo_single_job_analysis()
        elif demo_type == "comparison":
            demo_multiple_job_comparison()
        elif demo_type == "customization":
            demo_resume_customization()
        elif demo_type == "competitive":
            demo_competitive_analysis()
        elif demo_type == "roadmap":
            demo_learning_roadmap()
        elif demo_type == "strategy":
            demo_application_strategy()
        elif demo_type == "export":
            demo_export_functionality()
        elif demo_type == "all":
            # Run all demos
            demos = [
                demo_profile_overview,
                demo_single_job_analysis,
                demo_multiple_job_comparison,
                demo_resume_customization,
                demo_competitive_analysis,
                demo_learning_roadmap,
                demo_application_strategy,
                demo_export_functionality
            ]
            for demo_func in demos:
                demo_func()
                print("\n" + "⏸️ " * 20)
        else:
            print(f"Unknown demo type: {demo_type}")
            print("Available: profile, analysis, comparison, customization,")
            print("          competitive, roadmap, strategy, export, all")
    else:
        interactive_demo()

if __name__ == "__main__":
    main()