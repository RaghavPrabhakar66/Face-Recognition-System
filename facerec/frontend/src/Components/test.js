import { Menu } from '@headlessui/react'

const Test = () => {
	return (
		<div>
			<Menu>
				<Menu.Button >More</Menu.Button>
				<Menu.Items className="flex flex-col bg-orange-200">
					<Menu.Item>
						{({ active }) => (
							<a
								className={`${active && 'bg-blue-500'}`}
								href="/account-settings"
							>
								Account settings
							</a>
						)}
					</Menu.Item>
					<Menu.Item>
						{({ active }) => (
							<a
								className={`${active && 'bg-blue-500'}`}
								href="/account-settings"
							>
								Documentation
							</a>
						)}
					</Menu.Item>
					<Menu.Item disabled>
						<span className="opacity-75">Invite a friend (coming soon!)</span>
					</Menu.Item>
				</Menu.Items>
			</Menu>
		</div>
	);
};

export default Test;