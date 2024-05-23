from typing import TypeAlias

from cognite.neat.rules.models import DMSRules, DomainRules, InformationRules

Rules: TypeAlias = DomainRules | InformationRules | DMSRules
