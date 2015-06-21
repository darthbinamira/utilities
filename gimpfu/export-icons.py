location = '/home/darth/Blogs/darthbinamira.com/'
xcf_filename = 'favicon.xcf'
filename_pattern = '{}-{}x{}.png'
favicon_sizes = [192, 160, 96, 32, 16]
apple_touch_icon_sizes = [180, 152, 144, 120, 114, 76, 60, 72, 57]

def scale_and_save(image, sizes, prefix, location):
	for s in sizes:
		pdb.gimp_image_scale(image, s, s)
		pdb.file_png_save2(image, pdb.gimp_image_active_drawable(image), location + filename_pattern.format(prefix, s, s), filename_pattern.format(prefix, s, s), 0, 0, 0, 0, 0, 0, 1, 0, 1)


scale_and_save(pdb.gimp_xcf_load(1, location + xcf_filename, xcf_filename), favicon_sizes, 'favicon', location)
scale_and_save(pdb.gimp_xcf_load(1, location + xcf_filename, xcf_filename), apple_touch_icon_sizes, 'apple-touch-icon', location)

