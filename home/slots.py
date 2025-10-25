class Reservation(models.Model):
    # existing fields...

    @staticmethod
    def find_available_slots(restaurant_id, date, opening_hour, closing_hour, slot_duration_minutes=60):
        """
        Returns a list of available time slots for a given restaurant on a specific date.

        Args:
            restaurant_id (int): Restaurant ID to check availability
            date (datetime.date): Date for reservations
            opening_hour (datetime.time): Restaurant opening time
            closing_hour (datetime.time): Restaurant closing time
            slot_duration_minutes (int): Duration of each reservation slot

        Returns:
            List of tuples [(start_time, end_time), ...] for available slots
        """
        from datetime import datetime, timedelta, time

        # Fetch existing reservations for the restaurant on the given date
        reservations = Reservation.objects.filter(
            restaurant_id=restaurant_id,
            reservation_date=date
        )

        # Build a list of booked time ranges
        booked_slots = [(r.start_time, r.end_time) for r in reservations]

        # Generate all potential slots
        available_slots = []
        current_start = datetime.combine(date, opening_hour)
        closing_datetime = datetime.combine(date, closing_hour)
        delta = timedelta(minutes=slot_duration_minutes)

        while current_start + delta <= closing_datetime:
            current_end = current_start + delta
            overlap = any(
                (current_start.time() < end and current_end.time() > start)
                for start, end in booked_slots
            )
            if not overlap:
                available_slots.append((current_start.time(), current_end.time()))
            current_start += delta

        return available_slots
