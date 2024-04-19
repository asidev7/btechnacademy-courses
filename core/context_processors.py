

from core.models import Company, Service


def services(request):
    # Récupérer tous les objets Service
    services = Service.objects.all()[:4]
    # Renvoyer un dictionnaire avec les services
    return {'services': services}

def company(request):
    company = Company.objects.first()
    return {'company':company}