from accounts.models import PhaseDB

class Phasesave:
    def phase_save(self, phase_val, user_val, advertiser_val):
        phase_data = PhaseDB(phase_position=phase_val, phase_user_email=user_val,
                             phase_advertiser_name=advertiser_val)
        phase_data.save()
        print("phase saved...")
        for row in PhaseDB.objects.all().reverse():
            if PhaseDB.objects.filter(phase_user_email=user_val).count() > 1 \
                    and PhaseDB.objects.filter(phase_advertiser_name=advertiser_val).count() > 1:
                row.delete()
