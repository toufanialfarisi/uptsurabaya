. environment/bin/activate
echo "environemt was activated"
gunicorn app:app -b :5001 --workers 4 --reload