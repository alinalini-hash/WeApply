from app import db
from datetime import datetime
import json

class Questionnaire(db.Model):
    __tablename__ = 'questionnaires'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    
    # Berufserfahrung
    experience_level = db.Column(db.String(100))  # berufseinsteiger, berufserfahrener, führungskraft, praktikant, student
    years_of_experience = db.Column(db.Integer)  # Anzahl Jahre
    
    # Gehaltsvorstellung
    salary_min = db.Column(db.Integer)  # Minimum
    salary_max = db.Column(db.Integer)  # Maximum
    currency = db.Column(db.String(10), default='EUR')
    
    # Unternehmensvorlieben
    company_preferences = db.Column(db.Text)  # JSON: startup, konservativ, mittelstand, konzern, gemischt
    company_size = db.Column(db.String(100))  # startup, small, medium, large
    industry_preferences = db.Column(db.Text)  # JSON array
    
    # Arbeitsmodell
    remote_preference = db.Column(db.String(50))  # full-remote, hybrid, on-site
    contract_type = db.Column(db.String(50))  # permanent, contract, internship, freelance
    
    # Unternehmenskultur & Benefits
    culture_importance = db.Column(db.String(50))  # high, medium, low
    benefits_preferences = db.Column(db.Text)  # JSON array: health_insurance, gym, home_office, flexible_hours, stock_options
    
    # Dateien
    cv_path = db.Column(db.String(255))
    certificates_paths = db.Column(db.Text)  # JSON array
    
    # Metadaten
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_complete = db.Column(db.Boolean, default=False)  # Fragebogen vollständig?
    
    def get_company_preferences(self):
        return json.loads(self.company_preferences) if self.company_preferences else []
    
    def set_company_preferences(self, prefs):
        self.company_preferences = json.dumps(prefs)
    
    def get_industry_preferences(self):
        return json.loads(self.industry_preferences) if self.industry_preferences else []
    
    def set_industry_preferences(self, prefs):
        self.industry_preferences = json.dumps(prefs)
    
    def get_certificates(self):
        return json.loads(self.certificates_paths) if self.certificates_paths else []
    
    def set_certificates(self, certs):
        self.certificates_paths = json.dumps(certs)
    
    def get_benefits_preferences(self):
        return json.loads(self.benefits_preferences) if self.benefits_preferences else []
    
    def set_benefits_preferences(self, prefs):
        self.benefits_preferences = json.dumps(prefs)
    
    def to_dict(self):
        return {
            'id': self.id,
            'experience_level': self.experience_level,
            'years_of_experience': self.years_of_experience,
            'salary_min': self.salary_min,
            'salary_max': self.salary_max,
            'currency': self.currency,
            'company_preferences': self.get_company_preferences(),
            'company_size': self.company_size,
            'industry_preferences': self.get_industry_preferences(),
            'remote_preference': self.remote_preference,
            'contract_type': self.contract_type,
            'culture_importance': self.culture_importance,
            'benefits_preferences': self.get_benefits_preferences(),
            'cv_path': self.cv_path,
            'certificates': self.get_certificates(),
            'is_complete': self.is_complete,
            'created_at': self.created_at.isoformat()
        }
