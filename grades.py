def clean_grades(values):
    """Garde uniquement les notes numériques comprises entre 0 et 20."""
    return [v for v in values if isinstance(v, (int, float)) and 0 <= v <= 20]


def average(values):
    """Calcule la moyenne des notes, ou None si la liste est vide."""
    grades = clean_grades(values)
    if not grades:
        return None
    return sum(grades) / len(grades)


def mention(avg):
    """Retourne la mention correspondant à la moyenne."""
    if avg is None:
        return "Aucune note"
    if avg < 10:
        return "Insuffisant"
    if avg < 14:
        return "Moyen"
    return "Bien"

def max_grade(values):
      """Retourne la plus grande note ou None."""
      if not values:
      return None
      return max(values)
