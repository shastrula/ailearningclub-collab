from alertmanager import AlertClient

client = AlertClient('http://alertmanager:9093')

def alert_on_high_latency(duration_ms):
    if duration_ms > 500:
        client.send_alert({
            'labels': {'severity': 'warning'},
            'annotations': {'summary': f'Latency: {duration_ms}ms'}
        })