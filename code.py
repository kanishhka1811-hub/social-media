def compute_analytics(user_events): 
    df = pd.DataFrame(user_events) 
    total_seen  = df['views'].sum() 
    total_liked = df['likes'].sum() 
 
    tech_count     = len(df[df['category'] == 'TECH']) 
    non_tech_count = len(df[df['category'] == 'NON-TECH']) 
    total          = tech_count + non_tech_count 
    tech_pct       = round((tech_count / total) * 100) 
    non_tech_pct   = 100 - tech_pct 
 
    top_category = 'Tech Events' if tech_pct > non_tech_pct else 'Non-Tech Events' 
 
    most_seen  = df.sort_values('views',  ascending=False).head(5) 
    most_liked = df.sort_values('likes',  ascending=False).head(5) 
 
    return { 
        'total_seen':    total_seen, 
        'total_liked':   total_liked, 
        'top_category':  top_category,
          'tech_pct':      tech_pct, 
        'non_tech_pct':  non_tech_pct, 
        'most_seen':     most_seen, 
        'most_liked':    most_liked