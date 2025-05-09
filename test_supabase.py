from supabase import create_client, Client

url = "https://wrmazsquxubyggpitqto.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndybWF6c3F1eHVieWdncGl0cXRvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDY1NTE5NTEsImV4cCI6MjA2MjEyNzk1MX0.NIbNdur3k0IlsC72xEQY7AiYEzsnwnqFZ3Ugeua4sCQ"

supabase: Client = create_client(url, key)
print("✅ Connected to Supabase successfully")
