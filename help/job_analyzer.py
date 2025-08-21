#!/usr/bin/env python3
"""
Interactive Job Analysis Tool for Sachin Kumar's Profile
Provides easy-to-use interface for analyzing job descriptions
"""

import sys
import json
from datetime import datetime
from skills_matcher import SachinProfile, SkillsMatcher, ResumeCustomizer

class JobAnalyzer:
    """Interactive job analysis interface"""
    
    def __init__(self):
        self.profile = SachinProfile()
        self.matcher = SkillsMatcher(self.profile)
        self.customizer = ResumeCustomizer(self.profile)
        self.analysis_history = []
    
    def analyze_job_from_text(self, job_text: str, job_title: str = "iOS/macOS Developer"):
        """Analyze job description from text input"""
        print(f"\n🔍 Analyzing: {job_title}")
        print("=" * 60)
        
        match_result = self.matcher.match_job(job_text, job_title)
        
        # Store in history
        self.analysis_history.append({
            "timestamp": datetime.now().isoformat(),
            "job_title": job_title,
            "match_score": match_result.overall_score,
            "critical_missing": len(match_result.missing_critical_skills),
            "recommendations_count": len(match_result.recommendations)
        })
        
        self._display_results(match_result)
        return match_result
    
    def analyze_job_from_file(self, file_path: str, job_title: str = ""):
        """Analyze job description from file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                job_text = file.read()
            
            if not job_title:
                job_title = f"Job from {file_path}"
            
            return self.analyze_job_from_text(job_text, job_title)
        
        except FileNotFoundError:
            print(f"❌ Error: File '{file_path}' not found.")
            return None
        except Exception as e:
            print(f"❌ Error reading file: {e}")
            return None
    
    def _display_results(self, match_result):
        """Display analysis results in a formatted way"""
        
        # Overall score with color coding
        score = match_result.overall_score
        if score >= 80:
            score_emoji = "🟢"
        elif score >= 60:
            score_emoji = "🟡"
        else:
            score_emoji = "🔴"
        
        print(f"{score_emoji} OVERALL MATCH: {score:.1f}%")
        print(f"📊 RECOMMENDATION: {self._get_application_recommendation(score)}")
        
        # Category breakdown
        print("\n📈 SKILL CATEGORY BREAKDOWN:")
        for category, category_score in match_result.category_scores.items():
            bar = self._create_progress_bar(category_score)
            print(f"  {category.value.replace('_', ' ').title()}: {bar} {category_score:.1f}%")
        
        # Matched skills (top strengths)
        print(f"\n✅ YOUR STRENGTHS ({len(match_result.matched_skills)} matches):")
        top_skills = sorted(match_result.matched_skills, key=lambda x: x.proficiency, reverse=True)[:8]
        for i, skill in enumerate(top_skills, 1):
            proficiency_bar = "●" * (skill.proficiency // 2) + "○" * (5 - skill.proficiency // 2)
            print(f"  {i:2d}. {skill.name:<20} {proficiency_bar} ({skill.proficiency}/10)")
        
        # Critical gaps
        if match_result.missing_critical_skills:
            print(f"\n🚨 CRITICAL SKILL GAPS ({len(match_result.missing_critical_skills)}):")
            for i, skill in enumerate(match_result.missing_critical_skills[:6], 1):
                print(f"  {i}. {skill}")
            
            if len(match_result.missing_critical_skills) > 6:
                print(f"  ... and {len(match_result.missing_critical_skills) - 6} more")
        
        # Learning priorities
        print("\n🎯 PRIORITY ACTIONS:")
        for i, rec in enumerate(match_result.recommendations[:5], 1):
            print(f"  {i}. {rec}")
        
        # Competitive advantages
        if match_result.competitive_advantages:
            print("\n🏆 YOUR COMPETITIVE EDGE:")
            for adv in match_result.competitive_advantages:
                print(f"  • {adv}")
        
        # Interview preparation
        print("\n🎤 INTERVIEW PREPARATION:")
        for focus in match_result.interview_focus_areas[:4]:
            print(f"  • {focus}")
        
        # Application strategy
        print(f"\n📋 APPLICATION STRATEGY:")
        self._display_application_strategy(match_result)
    
    def _get_application_recommendation(self, score: float) -> str:
        """Get application recommendation based on score"""
        if score >= 85:
            return "EXCELLENT FIT - Apply immediately!"
        elif score >= 75:
            return "STRONG FIT - Apply with confidence"
        elif score >= 65:
            return "GOOD FIT - Apply with targeted preparation"
        elif score >= 50:
            return "MODERATE FIT - Consider learning key skills first"
        else:
            return "WEAK FIT - Focus on skill development before applying"
    
    def _create_progress_bar(self, percentage: float, width: int = 15) -> str:
        """Create a visual progress bar"""
        filled = int(width * percentage / 100)
        bar = "█" * filled + "░" * (width - filled)
        return f"[{bar}]"
    
    def _display_application_strategy(self, match_result):
        """Display tailored application strategy"""
        score = match_result.overall_score
        
        if score >= 75:
            print("  ✅ Priority: HIGH - Apply within 1-2 days")
            print("  📝 Cover letter: Emphasize your MDM expertise and Swift proficiency")
            print("  ⏱️ Timeline: Expect to hear back within 1-2 weeks")
        elif score >= 60:
            print("  ⚠️ Priority: MEDIUM - Apply after addressing critical gaps")
            print("  📚 Preparation: 1-2 weeks of targeted learning recommended")
            print("  📝 Cover letter: Address missing skills with learning commitment")
        else:
            print("  ⏳ Priority: LOW - Significant skill development needed")
            print("  📚 Preparation: 1-3 months of learning recommended")
            print("  🎯 Focus: Build portfolio projects demonstrating missing skills")
    
    def compare_jobs(self, job_results: list):
        """Compare multiple job analysis results"""
        if len(job_results) < 2:
            print("Need at least 2 job analyses to compare.")
            return
        
        print("\n🔄 JOB COMPARISON ANALYSIS")
        print("=" * 60)
        
        # Sort by match score
        sorted_jobs = sorted(job_results, key=lambda x: x.overall_score, reverse=True)
        
        print("📊 RANKING BY MATCH SCORE:")
        for i, result in enumerate(sorted_jobs, 1):
            score_emoji = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}."
            print(f"  {score_emoji} {result.job_title}: {result.overall_score:.1f}%")
        
        # Best fit analysis
        best_match = sorted_jobs[0]
        print(f"\n🎯 BEST FIT: {best_match.job_title}")
        print(f"  • Match Score: {best_match.overall_score:.1f}%")
        print(f"  • Missing Critical: {len(best_match.missing_critical_skills)} skills")
        print(f"  • Competitive Advantages: {len(best_match.competitive_advantages)}")
    
    def save_analysis(self, match_result, filename: str = None):
        """Save analysis results to file"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"job_analysis_{timestamp}.json"
        
        analysis_data = {
            "timestamp": datetime.now().isoformat(),
            "job_title": match_result.job_title,
            "overall_score": match_result.overall_score,
            "category_scores": {k.value: v for k, v in match_result.category_scores.items()},
            "matched_skills": [{"name": s.name, "proficiency": s.proficiency} for s in match_result.matched_skills],
            "missing_critical_skills": match_result.missing_critical_skills,
            "missing_nice_to_have": match_result.missing_nice_to_have,
            "recommendations": match_result.recommendations,
            "competitive_advantages": match_result.competitive_advantages,
            "interview_focus_areas": match_result.interview_focus_areas
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(analysis_data, f, indent=2)
            print(f"💾 Analysis saved to: {filename}")
        except Exception as e:
            print(f"❌ Error saving analysis: {e}")
    
    def show_profile_summary(self):
        """Display Sachin's profile summary"""
        print("\n👨‍💻 SACHIN KUMAR - PROFILE SUMMARY")
        print("=" * 50)
        print(f"📍 Location: {self.profile.personal_info['location']}")
        print(f"💼 Experience: {self.profile.personal_info['experience_years']} years")
        print(f"🎯 Specialization: {self.profile.personal_info['title']}")
        
        print("\n🔧 TOP SKILLS:")
        top_skills = sorted(self.profile.skills, key=lambda x: x.proficiency, reverse=True)[:10]
        for skill in top_skills:
            if skill.is_critical:
                print(f"  ⭐ {skill.name} ({skill.proficiency}/10) - {skill.years_experience}y exp")
            else:
                print(f"  • {skill.name} ({skill.proficiency}/10) - {skill.years_experience}y exp")
        
        print(f"\n📱 PROJECTS ({len(self.profile.projects)}):")
        for proj in self.profile.projects:
            print(f"  • {proj['name']}: {proj['description']}")
        
        print(f"\n📊 ANALYSIS HISTORY ({len(self.analysis_history)} jobs analyzed):")
        if self.analysis_history:
            for analysis in self.analysis_history[-5:]:  # Show last 5
                date = datetime.fromisoformat(analysis['timestamp']).strftime("%Y-%m-%d %H:%M")
                print(f"  • {date}: {analysis['job_title']} ({analysis['match_score']:.1f}%)")

def interactive_mode():
    """Run in interactive mode"""
    analyzer = JobAnalyzer()
    
    print("🚀 SACHIN'S SKILLS MATCHER - INTERACTIVE MODE")
    print("=" * 55)
    analyzer.show_profile_summary()
    
    job_results = []
    
    while True:
        print("\n" + "="*50)
        print("OPTIONS:")
        print("1. Analyze job from text input")
        print("2. Analyze job from file")
        print("3. Compare analyzed jobs")
        print("4. Show profile summary")
        print("5. Save last analysis")
        print("6. Exit")
        
        choice = input("\nSelect option (1-6): ").strip()
        
        if choice == "1":
            print("\nPaste the job description (press Enter twice when done):")
            lines = []
            while True:
                line = input()
                if line == "" and len(lines) > 0 and lines[-1] == "":
                    break
                lines.append(line)
            
            job_text = "\n".join(lines[:-1])  # Remove last empty line
            job_title = input("Job title (optional): ").strip()
            
            if job_text.strip():
                result = analyzer.analyze_job_from_text(job_text, job_title or "Job Analysis")
                if result:
                    job_results.append(result)
        
        elif choice == "2":
            file_path = input("Enter file path: ").strip()
            job_title = input("Job title (optional): ").strip()
            
            result = analyzer.analyze_job_from_file(file_path, job_title)
            if result:
                job_results.append(result)
        
        elif choice == "3":
            if len(job_results) >= 2:
                analyzer.compare_jobs(job_results)
            else:
                print("❌ Need at least 2 job analyses to compare.")
        
        elif choice == "4":
            analyzer.show_profile_summary()
        
        elif choice == "5":
            if job_results:
                last_result = job_results[-1]
                filename = input("Filename (press Enter for auto-generated): ").strip()
                analyzer.save_analysis(last_result, filename or None)
            else:
                print("❌ No analysis to save.")
        
        elif choice == "6":
            print("👋 Goodbye! Good luck with your job applications!")
            break
        
        else:
            print("❌ Invalid option. Please select 1-6.")

def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        # Command line mode
        analyzer = JobAnalyzer()
        
        if sys.argv[1] == "--file" and len(sys.argv) > 2:
            file_path = sys.argv[2]
            job_title = sys.argv[3] if len(sys.argv) > 3 else ""
            analyzer.analyze_job_from_file(file_path, job_title)
        
        elif sys.argv[1] == "--profile":
            analyzer.show_profile_summary()
        
        else:
            print("Usage:")
            print("  python job_analyzer.py --file <path> [job_title]")
            print("  python job_analyzer.py --profile")
            print("  python job_analyzer.py  (for interactive mode)")
    
    else:
        # Interactive mode
        interactive_mode()

if __name__ == "__main__":
    main()