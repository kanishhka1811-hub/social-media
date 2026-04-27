def build_dashboard(root, analytics): 
    # Metric Cards 
    tk.Label(root, text=str(analytics['total_seen']), 
             font=('Arial', 36, 'bold'), fg='#00BFFF').pack() 
    tk.Label(root, text='TOTAL SEEN').pack() 
 
    tk.Label(root, text=str(analytics['total_liked']), 
             font=('Arial', 36, 'bold'), fg='#FF69B4').pack() 
    tk.Label(root, text='TOTAL LIKED').pack() 
 
    tk.Label(root, text=analytics['top_category'], 
             font=('Arial', 24, 'bold'), fg='#9B59B6').pack() 
    tk.Label(root, text='TOP CATEGORY').pack() 
 
    # Ratio Bar using Matplotlib 
    fig, ax = plt.subplots(figsize=(8, 0.6)) 
    ax.barh([''], [analytics['tech_pct']], color='#00BFFF', label='Tech') 
    ax.barh([''], [analytics['non_tech_pct']], 
            left=[analytics['tech_pct']], color='#FF69B4', label='Non-Tech') 
    ax.axis('off') 
    canvas = FigureCanvasTkAgg(fig, master=root) 
    canvas.draw() 
    canvas.get_tk_widget().pack() 
 
    # Leaderboards 
    for i, row in analytics['most_seen'].iterrows(): 
        tk.Label(root, 
                 text=f"#{i+1}  {row['name']}  {row['views']} views  
[{row['category']}]" 
                 ).pack(anchor='w') 
 
root = tk.Tk() 
root.title('Interest Analytics Dashboard') 
analytics = compute_analytics(events) 
build_dashboard(root, analytics) 
root.mainloop() 
 
  
