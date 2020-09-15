from accounts.models import PhaseDB
from logger_settings import api_logger


class Phasesave:

    def phase_save(self, phase_val, user_val, advertiser_val):
        try:
            phase_data = PhaseDB(phase_position=phase_val, phase_user_email=user_val,
                                 phase_advertiser_name=advertiser_val)
            phase_data.save()
            api_logger.info("Phase has been saved in database...")
            for row in PhaseDB.objects.all().reverse():
                if PhaseDB.objects.filter(phase_user_email=user_val).count() > 1 \
                        and PhaseDB.objects.filter(phase_advertiser_name=advertiser_val).count() > 1:
                    row.delete()

        except Exception as e:
            api_logger.exception("Exception in saving phase in database..." + str(e))
