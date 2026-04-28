


# create your view here 

from django.shortcuts import render, redirect

def home(request):

    problems = [
        "Electrical points finalized too late",
        "Storage underestimated",
        "Budget increasing after work starts",
        "Carpenter coordination stress",
        "Layout changes during execution",
        "Quotation gaps are not addressed",
        "Compulsive pushing of new items or designs",
    ]

    icon_users = '<svg xmlns="http://www.w3.org/2000/svg" style="height:20px;width:20px;color:#ffffff;flex-shrink:0;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>'

    icon_layout = '<svg xmlns="http://www.w3.org/2000/svg" style="height:20px;width:20px;color:#ffffff;flex-shrink:0;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><line x1="3" x2="21" y1="9" y2="9"/><line x1="9" x2="9" y1="21" y2="9"/></svg>'

    icon_table = '<svg xmlns="http://www.w3.org/2000/svg" style="height:20px;width:20px;color:#ffffff;flex-shrink:0;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><path d="M3 9h18"/><path d="M3 15h18"/><path d="M9 3v18"/><path d="M15 3v18"/></svg>'

    icon_help = '<svg xmlns="http://www.w3.org/2000/svg" style="height:20px;width:20px;color:#ffffff;flex-shrink:0;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>'

    icon_rupee = '<svg xmlns="http://www.w3.org/2000/svg" style="height:20px;width:20px;color:#ffffff;flex-shrink:0;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h12"/><path d="M6 8h12"/><path d="m6 13 8.5 8"/><path d="M6 13h3"/><path d="M9 13c6.667 0 6.667-10 0-10"/></svg>'

    icon_clock = '<svg xmlns="http://www.w3.org/2000/svg" style="height:20px;width:20px;color:#ffffff;flex-shrink:0;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>'

    icon_git = '<svg xmlns="http://www.w3.org/2000/svg" style="height:20px;width:20px;color:#ffffff;flex-shrink:0;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="6" x2="6" y1="3" y2="15"/><circle cx="18" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M18 9a9 9 0 0 1-9 9"/></svg>'

    icon_clip = '<svg xmlns="http://www.w3.org/2000/svg" style="height:20px;width:20px;color:#ffffff;flex-shrink:0;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="8" height="4" x="8" y="2" rx="1" ry="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="m9 14 2 2 4-4"/></svg>'

    icon_cal = '<svg xmlns="http://www.w3.org/2000/svg" style="height:20px;width:20px;color:#ffffff;flex-shrink:0;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/><path d="m9 16 2 2 4-4"/></svg>'

    icon_shield = '<svg xmlns="http://www.w3.org/2000/svg" style="height:20px;width:20px;color:#ffffff;flex-shrink:0;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>'

    icon_file = '<svg xmlns="http://www.w3.org/2000/svg" style="height:20px;width:20px;color:#ffffff;flex-shrink:0;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/><polyline points="14 2 14 8 20 8"/><line x1="16" x2="8" y1="13" y2="13"/><line x1="16" x2="8" y1="17" y2="17"/><line x1="10" x2="8" y1="9" y2="9"/></svg>'

    icon_search = '<svg xmlns="http://www.w3.org/2000/svg" style="height:20px;width:20px;color:#ffffff;flex-shrink:0;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/><path d="m8 11 2 2 4-4"/></svg>'

    icon_sm = '<svg xmlns="http://www.w3.org/2000/svg" style="height:20px;width:20px;color:#ffffff;flex-shrink:0;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>'
    # icon_users = '<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-primary" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>'
    # icon_layout = '<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-primary" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><line x1="3" x2="21" y1="9" y2="9"/><line x1="9" x2="9" y1="21" y2="9"/></svg>'
    # icon_table = '<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-primary" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><path d="M3 9h18"/><path d="M3 15h18"/><path d="M9 3v18"/><path d="M15 3v18"/></svg>'
    # icon_help = '<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-primary" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>'
    # icon_rupee = '<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-primary" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h12"/><path d="M6 8h12"/><path d="m6 13 8.5 8"/><path d="M6 13h3"/><path d="M9 13c6.667 0 6.667-10 0-10"/></svg>'
    # icon_clock = '<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-primary" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>'
    # icon_git = '<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-primary" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="6" x2="6" y1="3" y2="15"/><circle cx="18" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M18 9a9 9 0 0 1-9 9"/></svg>'

    delay_reasons = [
        {"icon": icon_users, "text": "Designers handling too many flats at the same time"},
        {"icon": icon_layout, "text": "Execution starting before layouts are fully finalized"},
        {"icon": icon_table, "text": "Site readiness not done before execution planning"},
        {"icon": icon_help, "text": "MDF vs Plywood confusion"},
        {"icon": icon_rupee, "text": "Budget mismatches discovered mid-project"},
        {"icon": icon_clock, "text": "Aggressive timelines promised to close the deal"},
        {"icon": icon_git, "text": "Poor coordination between teams"},
    ]

    icon_sm = '<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>'

    execution_gaps = [
        {
            "icon": icon_clock,
            "title": "Timeline Commitment Issues",
            "points": [
                "No written completion date or milestone tracking",
                "Verbal promises without structured schedules",
            ],
            "highlight": "If a completion date is not documented clearly, delays are not unexpected — they are likely."
        },
        {
            "icon": icon_git,
            "title": "Site Coordination Gaps",
            "points": [
                "Multiple vendors working without central coordination",
                "Electrician, carpenter and civil work not aligned",
                "Frequent on-site corrections due to miscommunication",
            ],
            "highlight": "Good interiors don't require you to visit the site every evening to 'check what's happening.'"
        },
        {
            "icon": icon_rupee,
            "title": "Scope Creep During Execution",
            "points": [
                "Design changes happening mid-execution",
                "Additions increasing budget unexpectedly",
                "Items assumed but not documented in scope",
            ],
            "highlight": "Most cost escalations don't appear suddenly — they start with unclear scope."
        },
        {
            "icon": icon_help,
            "title": "Quality Control Gaps",
            "points": [
                "No site supervision process",
                "No stage-wise quality checks",
                "Work accepted without inspection",
            ],
            "highlight": "On-time interiors come from process — not luck or last-minute corrections."
        },
        {
            "icon": icon_users,
            "title": "Client Stress & Double Moving",
            "points": [
                "Shifting into an unfinished home",
                "Living inside an active worksite",
                "Moving twice because interiors weren't ready",
            ],
            "highlight": "Possession is fixed. Execution must be aligned to it."
        },
    ]

    # icon_clip = '<svg xmlns="http://www.w3.org/2000/svg" style="height:20px;width:20px;stroke:#ffffff;flex-shrink:0;" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="8" height="4" x="8" y="2" rx="1" ry="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="m9 14 2 2 4-4"/></svg>'
    # icon_cal = '<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/><path d="m9 16 2 2 4-4"/></svg>'
    # icon_shield = '<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>'
    # icon_file = '<svg xmlns="http://www.w3.org/2000/svg" style="height:20px;width:20px;stroke:#ffffff;flex-shrink:0;" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/><polyline points="14 2 14 8 20 8"/><line x1="16" x2="8" y1="13" y2="13"/><line x1="16" x2="8" y1="17" y2="17"/><line x1="10" x2="8" y1="9" y2="9"/></svg>'
    # icon_search = '<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/><path d="m8 11 2 2 4-4"/></svg>'

    pillars = [
        {"icon": icon_clip, "title": "Defined Scope Before Work Begins", "desc": "Every element is documented through a detailed BOQ, layout freeze and scope confirmation.", "highlight": "This reduces mid-project additions, assumption gaps and budget escalation."},
        {"icon": icon_cal, "title": "Written Timeline With Milestones", "desc": "We define realistic execution schedules and milestone checkpoints before site work begins.", "highlight": "A completion timeline is not verbal — it is planned and tracked."},
        {"icon": icon_users, "title": "Centralised Vendor Coordination", "desc": "M.E.P, furniture production, electrical, plumbing and finishing are aligned under one coordinated execution flow.", "highlight": "This prevents last-minute corrections and rework."},
        {"icon": icon_file, "title": "Documented Material Specifications", "desc": "Material brands, grades and hardware details are clearly defined before execution.", "highlight": "What is specified is what gets installed."},
        {"icon": icon_shield, "title": "Controlled Project Load", "desc": "We limit the number of simultaneous projects to maintain supervision and quality control.", "highlight": "Execution suffers when attention is divided."},
        {"icon": icon_search, "title": "Stage-Wise Quality Checks", "desc": "Work is reviewed at defined stages rather than at the end — reducing compounding mistakes.", "highlight": "Small corrections early prevent expensive fixes later."},
    ]

    checklist = [
        {"icon": icon_clip, "text": "Is the scope finalized before work starts?"},
        {"icon": icon_file, "text": "Are materials clearly defined in writing?"},
        {"icon": icon_git, "text": "Is it modular or carpentry style execution?"},
        {"icon": icon_layout, "text": "End-to-end layouts given beforehand?"},
        {"icon": icon_clock, "text": "Is the timeline realistic based on scope?"},
    ]

    qualifiers = [
        "New flat/Villa owners",
        "End-to-end re-model",
        "Possession within 3 months",
        "Looking for structured, stress-free interiors",
    ]

    testimonials = [
        {"name": "Krishna", "initials": "RK", "text": "Exceptional work! They transformed our 3BHK into a dream home. The attention to detail and quality of materials used was outstanding."},
        {"name": "Rajendra Prasad", "initials": "RP", "text": "Professional team and timely delivery. Our modular kitchen is exactly what we envisioned. Highly recommend their services!"},
        {"name": "Amit Patel", "initials": "AP", "text": "From concept to handover, everything was seamless. The 10-year warranty gave us peace of mind. Worth every rupee!"},
        {"name": "Ravi", "initials": "SR", "text": "Amazing design sense and execution. They helped us choose from 1200+ combos and created a unique space for our family."},
        {"name": "Shekar", "initials": "VS", "text": "Post-handover support is excellent. Any minor issues were resolved immediately. True professionals in every sense!"},
    ]

    reels = [
        {"title": "Kitchen Transformation", "video": "videos/reel-1.mp4"},
        {"title": "Modern Living Room", "video": "videos/reel-2.mp4"},
        {"title": "Luxury Bedroom Journey", "video": "videos/reel-3.mp4"},
        {"title": "Interior Design", "video": "videos/reel-4.mp4"},
        {"title": "Home Makeover", "video": "videos/reel-5.mp4"},
        {"title": "Island Kitchen Design", "video": "videos/reel-6.mp4"},
        {"title": "Wardrobe Design", "video": "videos/reel-7.mp4"},
        {"title": "Decor Inspiration", "video": "videos/reel-8.mp4"},
        {"title": "Living Space Design", "video": "videos/reel-9.mp4"},
        {"title": "Production Day", "video": "videos/reel-10.mp4"},
    ]

    faqs = [
        {"q": "Do you provide BOQ?", "a": "Yes. All materials and scope are clearly defined before execution."},
        {"q": "How long does execution take?", "a": "Typically 45–60 days depending on scope."},
        {"q": "Is pricing fixed?", "a": "Yes. Scope is finalized before work begins to avoid escalation."},
        {"q": "Do you handle full execution?", "a": "Yes. We manage design, coordination and execution."},
    ]

    realtalk_items = [
    {
        "num": "01",
        "tag": "Pricing",
        "question": "They'll just inflate the quote to match whatever budget I tell them. How do you handle this?",
        "answer": "Quotes are built line-by-line from site measurements and material specifications — not from your budget number. Whether you share your budget or not, pricing is based on scope, dimensions, materials, and execution requirements. If budget needs adjustment, scope changes are discussed transparently.",
        "tip_icon": "📋",
        "tip": "Every quote includes a detailed BOQ listing material, brand, grade, quantity, and rates."
    },
    {
        "num": "02",
        "tag": "Sales Pressure",
        "question": "Offer valid for 3 days. Price revision coming. How do firms use urgency — and what's your policy?",
        "answer": "We do not use artificial urgency. A genuine proposal should allow you enough time to compare, evaluate, and make a calm decision. We encourage clients to compare multiple quotations before choosing.",
        "tip_icon": "🤝",
        "tip": "We recommend comparing at least 4–5 firms before making a final decision."
    },
    {
        "num": "03",
        "tag": "Hidden Commissions",
        "question": "Designers get commissions from brands they recommend. Are suggestions really neutral?",
        "answer": "This concern is valid in many cases. Our recommendations are based on on-site performance, reliability, service support, and durability — not commissions. All recommended brands are documented clearly in the BOQ.",
        "tip_icon": "🔍",
        "tip": "Always ask what plywood, laminate, hardware, or fittings are being proposed — and why."
    },
    {
        "num": "04",
        "tag": "Material Quality",
        "question": "How do I know you're using BWP plywood and not a cheaper substitute?",
        "answer": "Once materials are installed, verification becomes difficult. That is why material checks should happen before installation. Clients are welcome to inspect boards, hardware, laminates, and production-stage materials before execution.",
        "tip_icon": "✅",
        "tip": "Material specs should be locked in BOQ and physically verifiable before production."
    },
    {
        "num": "05",
        "tag": "Timelines",
        "question": "Timelines always slip. The 45-day promise is a lie. What makes yours different?",
        "answer": "Delays can happen due to civil readiness, approvals, or external dependencies. What matters is planning, milestone tracking, and early escalation. We create phase-wise schedules before execution begins and monitor progress systematically.",
        "tip_icon": "📅",
        "tip": "Ask every firm whether timelines are written into the agreement with milestone dates."
    },
    {
        "num": "06",
        "tag": "Money Protection",
        "question": "A contractor took advance money, did partial work, then disappeared.",
        "answer": "This is why payments should always be milestone-linked. Payments must move only when clearly defined stages are completed and verified. Excessive upfront payment demands are a warning sign.",
        "tip_icon": "🔒",
        "tip": "Best structure: mobilisation advance → stage payments → final payment after handover."
    },
    {
        "num": "07",
        "tag": "Design vs Execution",
        "question": "Design is outsourced, execution is outsourced, and no one is accountable when issues happen.",
        "answer": "This split responsibility causes confusion in many projects. A turnkey structure works best when one team owns design coordination, execution quality, and final handover responsibility.",
        "tip_icon": "🎯",
        "tip": "Ask who supervises daily execution and who owns mismatch issues."
    },
    {
        "num": "08",
        "tag": "Mid-Project Changes",
        "question": "Design kept changing during execution and budget exploded. How do you prevent scope creep?",
        "answer": "The best prevention is complete design freeze before execution starts. Layouts, elevations, materials, finishes, and functional details should be approved before production begins. Later changes should follow written revisions with clear cost and timeline impact.",
        "tip_icon": "🔏",
        "tip": "No verbal changes. Every revision should be documented."
    },
    {
        "num": "09",
        "tag": "Visiting Active Sites",
        "question": "Completed showrooms look nice. Can I visit an active production assembly ?",
        "answer": "This is one of the smartest things a client can ask. Ongoing assembly of furniture reveal cleanliness, supervision quality, worker discipline, coordination systems, and real workmanship standards.",
        "tip_icon": "🏗️",
        "tip": "Ask to see an active site before signing with any company."
    },
    {
        "num": "10",
        "tag": "After Handover",
        "question": "Many firms disappear after final payment. What happens if something breaks later?",
        "answer": "Proper handover should include final inspection, snag list closure, and post-handover support terms. Clients should know response timelines, warranty scope, and support contact points in advance.",
        "tip_icon": "📞",
        "tip": "Ask to speak with a customer whose project was handed over 6–12 months ago."
    },
    {
        "num": "11",
        "tag": "Cheap vs Value",
        "question": "Cheap doesn't mean value. Expensive doesn't mean premium. What really matters?",
        "answer": "Correct comparison is never total price alone. The real comparison is plywood grade, hardware quality, laminate type, execution method, supervision standards, and after-sales support. Lower price with poor materials often becomes more expensive later.",
        "tip_icon": "⚖️",
        "tip": "Good interiors should last 10–15 years with minimal major rework."
    },
    ]
    realtalk_checks = [
    "Can I see a detailed BOQ before signing?",
    "Will you add a penalty clause for delays?",
    "Is payment milestone linked?",
    "Who supervises site daily?",
    "Can I visit during production and assembly ?",
    ]

    return render(request, 'pages/home.html', {
        'problems': problems,
        'delay_reasons': delay_reasons,
        'execution_gaps': execution_gaps,
        'pillars': pillars,
        'checklist': checklist,
        'qualifiers': qualifiers,
        'testimonials': testimonials,
        'reels': reels,
        'faqs': faqs,
        'realtalk_items': realtalk_items,
        'realtalk_checks': realtalk_checks,
    })


def terms(request):
    return render(request, 'pages/terms.html')

def privacy(request):
    return render(request, 'pages/privacy.html')

def custom_404(request, exception):
    return render(request, '404.html', status=404)
