def add_one(number):
    return number + 1


def clamp(value, low, high):
    """
    Return value limited to the range [low, high].
    
    Args:
        value: The value to clamp.
        low: The lower bound (inclusive).
        high: The upper bound (inclusive).
    
    Returns:
        The clamped value.
    
    Raises:
        ValueError: If low > high.
    """
    if low > high:
        raise ValueError(f"low ({low}) must be less than or equal to high ({high})")
    return max(low, min(value, high))
