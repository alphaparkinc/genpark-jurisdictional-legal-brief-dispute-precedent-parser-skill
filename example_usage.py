from client import JurisdictionalLegalBriefDisputePrecedentParserClient

def main():
    client = JurisdictionalLegalBriefDisputePrecedentParserClient()
    res = client.parse_litigation_precedents_and_draft_brief('B2B Cloud SLA Breach and Consequential Damages Claim')
    print('Brief ID: ' + res['brief_id'] + ' | ' + res['matter_title'])
    print('Court Precedents Cited: ' + str(res['cited_court_precedents_count']) + ' | Win Probability: ' + str(res['litigation_success_probability_pct']) + '%')
    print('Precedents: ' + ', '.join(res['cjue_case_law_citations']))

if __name__ == '__main__':
    main()
