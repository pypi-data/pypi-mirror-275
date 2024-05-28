#!/usr/bin/env python


########################################################################################################################


class SlackReport(object):
    def __init__(self, certs, warning, critical,
                 ok_symbol=":white_check_mark:",
                 error_symbol=":no_entry:",
                 warning_symbol=":warning:",
                 critical_symbol=":bangbang:",
                 expired_symbol=":rotating_light:",
                 skip_ok=False, title="SSL certificates report"):
        self.certs = certs
        self.warning = warning
        self.critical = critical
        self.skip_ok = skip_ok
        self.title = title
        self.ok_symbol = ok_symbol
        self.error_symbol = error_symbol
        self.warning_symbol = warning_symbol
        self.critical_symbol = critical_symbol
        self.expired_symbol = expired_symbol
        self.report = []

    def gen_report(self):
        for c in self.certs:
            name = c.get("name")
            expire_date = c.get("notAfter")
            days = c.get("expire_age")
            error_message = c.get("error_message")
            if error_message:
                row = f"{self.error_symbol} *{name}* - {error_message}"

            elif not error_message and isinstance(days, int) and days < 0:
                row = f"*{name}* - Will expire in {abs(days)} days ({expire_date})."
                if abs(days) <= self.critical:
                    row = f"{self.critical_symbol} {row}"
                elif self.warning >= abs(days) > self.critical:
                    row = f"{self.warning_symbol} {row}"
                elif self.skip_ok:
                    continue
                else:
                    row = f"{self.ok_symbol} {row}"

            elif not error_message and isinstance(days, int) and days >= 0:
                row = f"Cert **{name}** has already expired. Expired {abs(days)} days ago ({expire_date})."
                if abs(days) <= self.critical:
                    row = f"{self.expired_symbol} {row}"
            else:
                row = f"Unknown state for cert **{name}**."

            if row:
                row += "\n"
                self.report.append((days, row))

    def get_report_payload(self):
        rows = ""

        for e in sorted(self.report, reverse=True):
            rows += f"{e[-1]}\n"

        if rows:
            return {"text": f"*{self.title}*\n{rows}"}
